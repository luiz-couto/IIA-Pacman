
if [ -d ./benchmarks ];
then
    rm -rf ./benchmarks
fi

mkdir -p ./benchmarks

for fase in tinyMaze mediumMaze openMaze smallMaze contoursMaze bigMaze;
do

    for algo in bfs dfs ucs gs astar;
    do
        echo "Running $algo in $fase"
        START=$(date +%s.%N)
        python3 pacman.py --layout $fase --pacman SearchAgent --agentArgs fn=$algo >> ./benchmarks/$fase-benchmark.txt;
        END=$(date +%s.%N)
        DIFF=$(echo "$END - $START" | bc)
        echo "Total Time: $DIFF" >> ./benchmarks/$fase-benchmark.txt;
        echo -e "" >> ./benchmarks/$fase-benchmark.txt;
    done;
done


for fase in tinyMaze mediumMaze openMaze smallMaze contoursMaze bigMaze;
do

    for algo in gs astar;
    do
        for heu in manhattanHeuristic;
        do
            echo "Running $algo in $fase using $heu heuristic"
            START=$(date +%s.%N)
            python3 pacman.py --layout $fase --pacman SearchAgent --agentArgs fn=$algo,heuristic=$heu >> ./benchmarks/$fase-benchmark.txt;
            END=$(date +%s.%N)
            DIFF=$(echo "$END - $START" | bc)
            echo "Total Time: $DIFF" >> ./benchmarks/$fase-benchmark.txt;
            echo -e "" >> ./benchmarks/$fase-benchmark.txt;
        done;
    done;
done


for fase in trickySearch tinySearch smallSearch;
do
    for algo in foodHeuristic;
    do
        echo "Running $algo in $fase"
        START=$(date +%s.%N)
        python3 pacman.py --layout $fase --pacman SearchAgent --agentArgs fn=astar,prob=FoodSearchProblem,heuristic=$algo >> ./benchmarks/$fase-benchmark.txt;
        END=$(date +%s.%N)
        DIFF=$(echo "$END - $START" | bc)
        echo "Total Time: $DIFF" >> ./benchmarks/$fase-benchmark.txt;
        echo -e "" >> ./benchmarks/$fase-benchmark.txt;
    done;
done