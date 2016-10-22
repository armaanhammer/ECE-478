//Pathfinding algorithm

#include <iostream>
#include <iomanip>
#include <stdlib.h>
#include <stdio.h>
#include <vector>
#include <ctime>
#include <math.h>
#include <queue>


using namespace std;

const int MAP_WIDTH = 100;		//horizontal test map size
const int MAP_HEIGHT = 100;		//vertical test map size

static int closed_node_map[MAP_WIDTH][MAP_HEIGHT]; // map of closed (tried-out) nodes
static int open_node_map[MAP_WIDTH][MAP_HEIGHT];	// map of open (not-yet-tried) nodes
static int map[MAP_WIDTH][MAP_HEIGHT];				//n x m
static int Direction_map[MAP_WIDTH][MAP_HEIGHT];	//map of directionals


//directionals, this is two seperate arrays that contain pairs of directions for each map.  
//1 means move positive (right / up) 0 means no move, and -1 means negative (left, down)
//supported directions in order are:  up, diag up right , up, diag up left, left, diag down left, down, diag down right

//****************************************************************************
//*   \     |   /
//*   <--  []  -->
//*   /     |   \
//****************************************************************************
static int DirectionX[] = { 1, 1, 0,-1,-1,-1, 0, 1 };
static int DirectionY[] = { 0, 1, 1, 1, 0,-1,-1,-1 };
//directions
enum DIRECTION_COMMAND {MOVE_FORWARD, MOVE_BACK, MOVE_LEFT, MOVE_RIGHT, TURN_LEFT, TURN_RIGHT, 
	WALK_STOP, WALK_READY, WALK_SPEED_SLOW, WALK_SPEED_MEDIUM, WALK_SPEED_FAST};



class SearchNode
{
public:
		int NodePosX;	
		int NodePosY;			// current position of node being searched
		int level;
		int priority;
		
		//properties stub
		SearchNode(int xp, int yp, int d, int p)
		{
			NodePosX = xp;
			NodePosY = yp;
			level = d;
			priority = p;
		}
		int GetPriority() const { return priority; }
		int GetLevel() const { return level; }
		int getXPos() const { return NodePosX; }
		int getYPos() const { return NodePosY; }

		bool IsSameState(SearchNode &rhs);
		
		
		//get priority of nodes
		void updatePriority(const int & DestX, const int & DestY)
		{
			priority = level + estimate(DestX, DestY) * 10;
		}

		const int & estimate(const int & DestX, const int & DestY) const
		{
			static int xd, yd, d;
			xd = DestX - NodePosX;
			yd = DestY - NodePosY;
			//euclidian distance compute
			d = static_cast<int>(sqrt(xd*xd + yd*yd));
			return d;
		}
		
};

// Determine priority (in the priority queue)
bool operator<(const SearchNode & a, const SearchNode & b)
{
	return a.GetPriority() > b.GetPriority();
}


//search if the state is same
bool SearchNode::IsSameState(SearchNode &rhs)
{
	//same state is when x,y are the same.  
	if ((NodePosX == rhs.NodePosX) && (NodePosY == rhs.NodePosY))
	{
		return true;
	}
	else
	{
		return false;
	}
}


//the heart and soul of pathfinding.  Takes four arguments, which is simply the start coords, and the
//goal coords.  returns string/ map of directionals as the route 
string PathFinder(const int & StartX, const int & StartY, const int & GoalX, const int & GoalY)
{
	//make a priority queue
	static priority_queue<SearchNode> pq[2];
	static int pqIndex;
	static SearchNode* N0;			//node for Width  X
	static SearchNode* M0;			//node for height Y
	static int i, j, x, y, xdx, ydy;
	static char c;

	pqIndex = 0;

	//reset node maps
	for (y = 0; y < MAP_HEIGHT; y++)
	{
		for (x = 0; x < MAP_WIDTH; x++)
		{
			closed_node_map[x][y] = 0;
			open_node_map[x][y] = 0;
		}
	}

	//create new start node
	N0 = new SearchNode(StartX, StartY, 0, 0);
	N0->updatePriority(GoalX, GoalY);
	pq[pqIndex].push(*N0);
	open_node_map[StartX][StartY] = N0->GetPriority();

	while (!pq[pqIndex].empty())  //while not empty
	{
		//construct a new node 
		N0 = new SearchNode(pq[pqIndex].top().getXPos(), pq[pqIndex].top().getYPos,
			pq[pqIndex].top().GetLevel(), pq[pqIndex].top().GetPriority());

		x = N0->getXPos();
		y = N0->getYPos();

		pq[pqIndex].pop();		//remove node from open list
		open_node_map[x][y] = 0;
								//mark it on closed map
		closed_node_map[x][y] = 1;

		//terminate search when goal is reached
		if (x == GoalX && y == GoalY)
		{
			string path = "";
			while (!(x == StartX && y == StartY))
			{
				j = Direction_map[x][y];
				c = '0' + (j + direction / 2) % direction;
				path = c + path;
				x += DirectionX[j];
				y += DirectionY[j];


			}

			delete N0;
			//empty leftovers
			while (!pq[pqIndex].empty()) pq[pqIndex].pop();
			return path;
		}


		//generate moves for child



	}

}




int main()
{
	srand(time(NULL));

	//build an empty map
	for (int y = 0; y < MAP_HEIGHT; y++)
	{
		for (int x = 0; x < MAP_WIDTH; x++)
		{
			map[x][y] = 0;
		}
	}

	//fill map with + pattern
	for (int x = MAP_WIDTH / 8; x < MAP_WIDTH * 7 / 8; x++)
	{ 
		map[x][MAP_WIDTH / 2] = 1;
	}
	for (int y = MAP_HEIGHT / 8; y < MAP_HEIGHT * 7 / 8 y++)
	{
		map[MAP_WIDTH / 2][y] = 1;
	}

	// select the start and finish points as we receive from kinect data

	////////////////////////////////////////////////////////////////////
	
	
	cout << "Map Size (X, Y): " << MAP_WIDTH << MAP_HEIGHT << endl;

	// display the map with the route
	for (int y = 0; y< MAP_HEIGHT; y++)
	{
		for (int x = 0; x< MAP_WIDTH; x++)
			if (map[x][y] == 0)
				cout << ".";
			else if (map[x][y] == 1)
				cout << "O"; //obstacle
			else if (map[x][y] == 2)
				cout << "S"; //start
			else if (map[x][y] == 3)
				cout << "R"; //route
			else if (map[x][y] == 4)
				cout << "F"; //finish
			cout << endl;
	}


	//program is done when robot reaches the goal point
}




