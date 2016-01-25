// g++ -std=c++11 -O3 -L/usr/local/lib -I/usr/local/include/eigen3 -I/usr/local/include/libigl/include/ -I/usr/local/include/boost/ -I/usr/local/include/ slicing.cpp -lmpfr -lgmp -lCGAL -lboost_thread-mt -lboost_system-mt -o slicing



#include <igl/readOBJ.h>
#include <igl/writeOBJ.h>
#include <igl/boolean/mesh_boolean.h>
#include <Eigen/Core>
#include <Eigen/Geometry>
#include <fstream>
#include <sstream>

using namespace Eigen;
using namespace std;

struct CutNode
{
	CutNode() : lchild(NULL), rchild(NULL) {}
	~CutNode() {delete lchild; delete rchild;}

	Vector3d pt;
	Vector3d n;
	CutNode *lchild, *rchild;
};

struct LineInfo
{
	int lchild;
	int rchild;
	Vector3d pt;
	Vector3d n;
};

CutNode *buildCutTree(const vector<LineInfo> &lines, int curline)
{
	if(curline >= lines.size())
		return NULL;
	CutNode *result = new CutNode;
	result->pt = lines[curline].pt;
	result->n = lines[curline].n;
	result->lchild = buildCutTree(lines, lines[curline].lchild-1);
	result->rchild = buildCutTree(lines, lines[curline].rchild-1);
	return result;
}

CutNode *parseCutFile(char *filename)
{
	ifstream ifs(filename);
	if(!ifs)
		return NULL;

	vector<LineInfo> lines;
	while(true)
	{
		char c;
		LineInfo line;
		ifs >> line.lchild >> c >> line.rchild >> c >> line.pt[0] >> c >> line.pt[1] >> c >> line.pt[2] >> c >> line.n[0] >> c >> line.n[1] >> c >> line.n[2];
		if(!ifs)
			break;
		else
			lines.push_back(line);
	}
	return buildCutTree(lines,0);
}

Vector3d supportingPlane(const MatrixXd &V, const Vector3d &n)
{
	Vector3d result(0,0,0);
	int nverts = V.rows();

	double furthestdist = -numeric_limits<double>::infinity();

	for(int i=0; i<nverts; i++)
	{
		Vector3d pt = V.row(i);
		double proj = pt.dot(n);
		if(proj > furthestdist)
		{
			furthestdist = proj;
			result = pt;
		}
	}
	return result;
}

Vector3d findCorner(const Vector3d &side1pt, const Vector3d &side1dir, const Vector3d &side2pt, const Vector3d &side2dir, const Vector3d &side3pt, const Vector3d &side3dir)
{
	//(c - pi).di = 0
	Matrix3d M;
	M.row(0) = side1dir;
	M.row(1) = side2dir;
	M.row(2) = side3dir;
	Vector3d rhs;
	rhs[0] = side1dir.dot(side1pt);
	rhs[1] = side2dir.dot(side2pt);
	rhs[2] = side3dir.dot(side3pt);

	return M.inverse()*rhs;
}

void makeCube(const MatrixXd &V, const Vector3d &pt, const Vector3d &dir, double padding, MatrixXd &cubeV, MatrixXi &cubeF)
{
	int smallest = 0;
	double smallestval = fabs(dir[0]);
	for(int i=1; i<3; i++)
		if(fabs(dir[i]) < smallestval)
		{
			smallestval = fabs(dir[i]);
			smallest = i;
		}
	Vector3d crossvec(0,0,0);
	crossvec[smallest] = 1.0;
	Vector3d n = dir;
	n /= n.norm();
	Vector3d perp = n.cross(crossvec);
	perp /= perp.norm();
	Vector3d perp2 = -n.cross(perp);
	perp2 /= perp2.norm();

	Vector3d side1v = supportingPlane(V, perp);
	side1v += padding*perp;

	Vector3d side2v = supportingPlane(V, perp2);
	side2v += padding*perp2;

	Vector3d side3v = supportingPlane(V, -perp);
	side3v -= padding*perp;

	Vector3d side4v = supportingPlane(V, -perp2);
	side4v -= padding*perp2;

	cubeV.resize(8,3);
	cubeV.row(0) = findCorner(pt, n, side1v, perp, side2v, perp2);
	cubeV.row(1) = findCorner(pt, n, side2v, perp2, side3v, perp);
	cubeV.row(2) = findCorner(pt, n, side3v, perp, side4v,perp2);
	cubeV.row(3) = findCorner(pt, n, side4v, perp2, side1v, perp);
	Vector3d opppt = supportingPlane(V, n);
	opppt += padding*n;
	cubeV.row(4) = findCorner(opppt, n, side1v, perp, side2v, perp2);
	cubeV.row(5) = findCorner(opppt, n, side2v, perp2, side3v, perp);
	cubeV.row(6) = findCorner(opppt, n, side3v, perp, side4v,perp2);
	cubeV.row(7) = findCorner(opppt, n, side4v, perp2, side1v, perp);

	cubeF.resize(12, 3);

	cubeF << 0, 1, 2,
		2, 3, 0,
		0, 4, 5,
		0, 5, 1,
		1, 5, 6,
		1, 6, 2,
		2, 6, 7,
		2, 7, 3,
		3, 7, 4,
		3, 4, 0,
		4, 7, 6,
		4, 6, 5;
}

void performSlicing(const MatrixXd &V, const MatrixXi &F, const CutNode *cuttree, vector<MatrixXd> &piecesV, vector<MatrixXi> &piecesF)
{
	if(cuttree == NULL)
	{
		piecesV.push_back(V);
		piecesF.push_back(F);
		return;
	}

	MatrixXd cubeV;
	MatrixXi cubeF;
	makeCube(V, cuttree->pt, cuttree->n, 0.1, cubeV, cubeF);

	MatrixXd upperV;
	MatrixXi upperF;
	igl::boolean::mesh_boolean(V,F,cubeV,cubeF,igl::boolean::MESH_BOOLEAN_TYPE_INTERSECT,upperV,upperF);
	makeCube(V, cuttree->pt, -cuttree->n, 0.1, cubeV, cubeF);
	MatrixXd lowerV;
	MatrixXi lowerF;
	igl::boolean::mesh_boolean(V,F,cubeV,cubeF,igl::boolean::MESH_BOOLEAN_TYPE_INTERSECT,lowerV,lowerF);

	performSlicing(lowerV, lowerF, cuttree->lchild, piecesV, piecesF);
	performSlicing(upperV, upperF, cuttree->rchild, piecesV, piecesF);
}

Vector3d areaNormal(const MatrixXd &V, const MatrixXi &F, int face)
{
	Vector3d e1 = V.row(F(face,1)) - V.row(F(face,0));
	Vector3d e2 = V.row(F(face,2)) - V.row(F(face,0));
	Vector3d result = e1.cross(e2);
	return 0.5*result;
}

Vector3d calculatePrintingPlane(const MatrixXd &V, const MatrixXi &F, double clusterTol)
{
	int nfaces = F.rows();
	vector<Vector3d> clusterNormals;
	vector<double> clusterAreas;

	for(int i=0; i<nfaces; i++)
	{
		Vector3d n = areaNormal(V, F, i);
		double area = n.norm();
		n /= area;
		double proj = V.row(F(i,0)).dot(n);
		Vector3d supppt = supportingPlane(V, n);
		double suppproj = supppt.dot(n);
		if(suppproj - proj > clusterTol)
			continue;

		bool found = false;
		for(int j=0; j<clusterNormals.size(); j++)
		{
			if( (clusterNormals[j] - n).norm() <= clusterTol)
			{
				clusterAreas[j] += area;
				found = true;
				break;
			}
		}
		if(!found)
		{
			clusterNormals.push_back(n);
			clusterAreas.push_back(area);
		}
	}

	int largest = -1;
	double largestval = 0;
	for(int i=0; i<clusterAreas.size(); i++)
	{
		if(clusterAreas[i] > largestval)
		{
			largest = i;
			largestval = clusterAreas[i];
		}
	}

	if(largest != -1)
		return clusterNormals[largest];
	return Vector3d(0,0,0);
}

Matrix3d computeRotation(const Vector3d &newup)
{
	Matrix3d result;
	Vector3d n =newup;
	double norm = n.norm();
	if(norm == 0.0)
	{
		result.setIdentity();
		return result;
	}
	n /= norm;
	int minc = 0;
	double minval = fabs(n[0]);
	for(int i=1; i<3; i++)
		if(fabs(n[i]) < minval)
		{
			minval = fabs(n[i]);
			minc = i;
		}
	Vector3d pivot(0,0,0);
	pivot[minc] = 1.0;
	Vector3d axis1 = n.cross(pivot);
	axis1 /= axis1.norm();
	Vector3d axis2 = -n.cross(axis1);
	axis2 /= axis2.norm();
	result.row(0) = axis1;
	result.row(1) = axis2;
	result.row(2) = -n;
	return result;
}

double costFunction(const MatrixXd &V, const MatrixXi &F, double groundTol)
{
	int nfaces = F.rows();
	double cost = 0;
	double maxdot = 1.0/sqrt(2.0);
	Vector3d z(0,0,-1.0);
	for(int i=0; i<nfaces; i++)
	{
		Vector3d arean = areaNormal(V, F, i);
		double area = arean.norm();
		arean /= area;
		if( (z-arean).norm() < groundTol)
		{
			if(fabs(V( F(i,0), 2)) < groundTol)
				continue;
		}
		if(z.dot(arean) > maxdot)
			cost += area;
	}
	return cost;
}

int main(int argc, char *argv[])
{

	if(argc != 3)
	{
		cerr << "Usage: slicing (mesh .obj file) (cutting description .txt file)" << endl;
		return -1;
	}

	Eigen::MatrixXd V;
	Eigen::MatrixXi F;
	igl::readOBJ(argv[1], V, F);
	CutNode *cuttree = parseCutFile(argv[2]);
	if(cuttree == NULL)
	{
		cerr << "Couldn't read cutting description file" << endl;
		return -1;
	}

	vector<MatrixXd> piecesV;
	vector<MatrixXi> piecesF;

	performSlicing(V, F, cuttree, piecesV, piecesF);
	int pieces = piecesV.size();
	double totcost = 0;
	for(int i=0; i<pieces; i++)
	{
		Vector3d axis = calculatePrintingPlane(piecesV[i], piecesF[i], 1e-6);
		Matrix3d rot = computeRotation(axis);
		piecesV[i] = piecesV[i] * rot.transpose();
		double minz = numeric_limits<double>::infinity();
		for(int j=0; j<piecesV[i].rows(); j++)
			minz = min(minz, piecesV[i](j,2));
		for(int j=0; j<piecesV[i].rows(); j++)
			piecesV[i](j,2) -= minz;

		totcost += costFunction(piecesV[i], piecesF[i], 1e-6);

		stringstream ss;
		ss << "piece-" << i << ".obj";
		igl::writeOBJ(ss.str(), piecesV[i], piecesF[i]);
	}
	cout << totcost << endl;

	delete cuttree;
	return 0;
}
