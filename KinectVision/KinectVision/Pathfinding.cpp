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
const int Direction = 8;		//number of directions we can travel in

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

//directions to commands
enum DIRECTION_COMMAND {MOVE_FORWARD, MOVE_BACK, MOVE_LEFT, MOVE_RIGHT, TURN_LEFT, TURN_RIGHT, 
	WALK_STOP, WALK_READY, WALK_SPEED_SLOW, WALK_SPEED_MEDIUM, WALK_SPEED_FAST};



class SearchNode
{
public:
		int NodePosX;			//current position of node in X
		int NodePosY;			// current position of node being searched
		int level;				//distance traveled to reach node
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

		
		//get priority of nodes
		void updatePriority(const int & DestX, const int & DestY)
		{
			priority = level + estimate(DestX, DestY) * 10;
		}

		void nextLevel(const int & i) // i: direction
		{
			level += (Direction == 8 ? (i % 2 == 0 ? 10 : 14) : 10);
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
		//construct a new node begin searching!
		N0 = new SearchNode(pq[pqIndex].top().getXPos(), pq[pqIndex].top().getYPos,
			pq[pqIndex].top().GetLevel(), pq[pqIndex].top().GetPriority());

		x = N0->getXPos();
		y = N0->getYPos();

		pq[pqIndex].pop();													//remove node from open list
		open_node_map[x][y] = 0;
		closed_node_map[x][y] = 1;											//mark it on closed map

		//terminate search when goal is reached, condition checks and produces output.
		//of directionals
		if (x == GoalX && y == GoalY)
		{
			string path = "";
			while (!(x == StartX && y == StartY))
			{
				j = Direction_map[x][y];
				c = '0' + (j + Direction / 2) % Direction;
				path = c + path;
				x += DirectionX[j];
				y += DirectionY[j];

			}

			delete N0;
			//empty leftovers
			while (!pq[pqIndex].empty()) pq[pqIndex].pop();
			return path;
		}


		//generate moves for child in all possible directions
		for (i = 0; i < Direction; i++)
		{
			xdx = x + DirectionX[i];
			ydy = y + DirectionY[i];

			//generate edge cases, like if its on edge of map
			//like x is negative (not allowed, x is out of bounds, or map is 1, or closed map is 1
			if (!(xdx < 0 || xdx > MAP_WIDTH - 1 || ydy < 0 || ydy > MAP_HEIGHT - 1 || map[xdx][ydy] == 1 || closed_node_map[xdx][ydy] == 1))
			{
				M0 = new SearchNode(xdx, ydy, N0->GetLevel(), N0->GetPriority());
				M0->nextLevel(i);															//i is direction
				M0->updatePriority(GoalX, GoalY);

				//if not in open list add to it
				if (open_node_map[xdx][ydy] == 0)
				{
					open_node_map[xdx][ydy] = M0->GetPriority();
					pq[pqIndex].push(*M0);

					Direction_map[xdx][ydy] = (i + Direction / 2) % Direction;
				}
				else if (open_node_map[xdx][ydy] > M0->GetPriority())
				{
					//update priority info
					open_node_map[xdx][ydy] = M0->GetPriority();
					//update parent direction info
					Direction_map[xdx][ydy] = (i + Direction / 2) % Direction;

					// replace the node
					// by emptying one pq to the other one
					// except the node to be replaced will be ignored
					// and the new node will be pushed in instead
					while (!(pq[pqIndex].top().getXPos() == xdx &&
						pq[pqIndex].top().getYPos() == ydy))
					{
						pq[1 - pqIndex].push(pq[pqIndex].top());
						pq[pqIndex].pop();
					}
					pq[pqIndex].pop();

					//empty the larger size pq to smaller one
					if (pq[pqIndex].size() > pq[1 - pqIndex].size())
					{
						pqIndex = 1 - pqIndex;
					}
					while (!pq[pqIndex].empty())
					{
						pq[1 - pqIndex].push(pq[pqIndex].top());
						pq[pqIndex].pop();
					}
					pqIndex = 1 - pqIndex;
					pq[pqIndex].push(*M0);

				}
				delete M0;
			}

		}
		delete N0;

	}
	return "";			//no route found
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
	for (int y = MAP_HEIGHT / 8; y < MAP_HEIGHT * 7 / 8; y++)
	{
		map[MAP_WIDTH / 2][y] = 1;
	}

	// select the start and finish points as we receive from kinect data
	// randomly select start and finish locations
	int xA, yA, xB, yB;
	switch (rand() % 8)
	{
	case 0: xA = 0; yA = 0; xB = n - 1; yB = m - 1; break;
	case 1: xA = 0; yA = m - 1; xB = n - 1; yB = 0; break;
	case 2: xA = n / 2 - 1; yA = m / 2 - 1; xB = n / 2 + 1; yB = m / 2 + 1; break;
	case 3: xA = n / 2 - 1; yA = m / 2 + 1; xB = n / 2 + 1; yB = m / 2 - 1; break;
	case 4: xA = n / 2 - 1; yA = 0; xB = n / 2 + 1; yB = m - 1; break;
	case 5: xA = n / 2 + 1; yA = m - 1; xB = n / 2 - 1; yB = 0; break;
	case 6: xA = 0; yA = m / 2 - 1; xB = n - 1; yB = m / 2 + 1; break;
	case 7: xA = n - 1; yA = m / 2 + 1; xB = 0; yB = m / 2 - 1; break;
	}
	////////////////////////////////////////////////////////////////////
	
	
	cout << "Map Size (X, Y): " << MAP_WIDTH << MAP_HEIGHT << endl;
	cout << "Start: " << xA << yA << endl;
	cout << "Finish: " << xB << yB << endl;

	//obtain route, run clock and start pathfinder alg.  Algorithm is run
	
	clock_t start = clock();
	
	//send in the coords of start and finish, which is randomly generated for now.  
	//we can change this to reflect kinect values!
	string route = PathFinder(xA, yA, xB, yB);
	if (route == "");
		cout << "Empty Rout generated" << endl;
	
	clock_t end = clock();
	double time_elapsed = double(end - start);
	cout << "Time to calculate route (ms): " << time_elapsed << endl;
	cout << "Route: " << endl;
	cout <<route<< endl;


	//follow route and display it
	if (route.length() > 0)
	{
		int i; char c;
		int x = xA;
		int y = yA;
		map[x][y] = 2;		//basically set the start coordinates, 2 is the marker.
		for (int i = 0; i < route.length(); i++)
		{
			c = route.at(i);
			j = c - '0';
			x = x + DirectionX[j];
			y = y + DirectionY[j];
			map[x][y] = 3;		//3 is marker for ROUTE
		}

	}
	// display the map with the route, iterate through matrix
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
	getchar();				//wait for enter keypress
	return(0);

	//program is done when robot reaches the goal point
}




