# Run the commandline compiler and runtime for all Processing code.
# This isn't quite running unit tests, but the effect should be similar.
PROCESS = ~/processing-2.0b8/processing-java
SRC = c:\Cliff\OpenDSA\SourceCode\Processing
BUILD = c:\Cliff\OpenDSA\SourceCode\Processing\build

all: Trees Sorting Graphs

clean:
	-rm -rf build
	mkdir build

Trees: GenTree UFTest

Sorting: Inssort InssortKV Bubblesort Selsort Shellsort Mergesort MergesortOpt Quicksort Heapsort Binsort

Graphs: GraphDummy GraphTrav GraphTop GraphDijk GraphMCST


GenTree: build/GenTree/success

build/GenTree/success: Trees/GenTree.pde
	@echo "GenTree Test"
	-@rm -rf build/GenTree
	@mkdir build/GenTree
	@cp Trees/GenTree.pde build/GenTree

UFTest: build/UFTest/success

build/UFTest/success: Trees/ParPtrTree.pde Trees/UFTest.pde
	@echo "UFTest Test"
	-@rm -rf build/UFTest
	@mkdir build/UFTest
	@cp Trees/ParPtrTree.pde build/UFTest
	@cp Trees/UFTest.pde build/UFTest
	@$(PROCESS) --run --sketch="$(BUILD)/UFTest" --output="$(BUILD)/build" --force

Inssort: build/InssortTest/success

build/InssortTest/success: Sorting/Insertionsort.pde Sorting/SortTest.pde Utils/Swap.pde
	@echo "Inssort Test"
	-@rm -rf build/InssortTest
	@mkdir build/InssortTest
	@cp Sorting/Insertionsort.pde build/InssortTest
	@cp Sorting/SortTest.pde build/InssortTest/InssortTest.pde
	@cp Utils/Swap.pde build/InssortTest
	@$(PROCESS) --run --sketch="$(BUILD)/InssortTest" --output="$(BUILD)/build" --force

InssortKV: build/InssortKVTest/success

build/InssortKVTest/success: Sorting/InssortKV.pde Sorting/SortTestKV.pde Utils/KVPair.pde
	@echo "InssortKV Test"
	-@rm -rf build/InssortKVTest
	@mkdir build/InssortKVTest
	@cp Sorting/InssortKV.pde build/InssortKVTest
	@cp Utils/KVPair.pde build/InssortKVTest
	@cp Sorting/SortTestKV.pde build/InssortKVTest/InssortKVTest.pde
	@$(PROCESS) --run --sketch="$(BUILD)/InssortKVTest" --output="$(BUILD)/build" --force

Bubblesort: build/BubblesortTest/success

build/BubblesortTest/success: Sorting/Bubblesort.pde Sorting/SortTest.pde Utils/Swap.pde
	@echo "Bubblesort Test"
	-@rm -rf build/BubblesortTest
	@mkdir build/BubblesortTest
	@cp Sorting/Bubblesort.pde build/BubblesortTest
	@cp Sorting/SortTest.pde build/BubblesortTest/BubblesortTest.pde
	@cp Utils/Swap.pde build/BubblesortTest
	@$(PROCESS) --run --sketch="$(BUILD)/BubblesortTest" --output="$(BUILD)/build" --force

Selsort: build/SelsortTest/success

build/SelsortTest/success: Sorting/Selectionsort.pde Sorting/SortTest.pde Utils/Swap.pde
	@echo "Selsort Test"
	-@rm -rf build/SelsortTest
	@mkdir build/SelsortTest
	@cp Sorting/Selectionsort.pde build/SelsortTest
	@cp Utils/Swap.pde build/SelsortTest
	@cp Sorting/SortTest.pde build/SelsortTest/SelsortTest.pde
	@$(PROCESS) --run --sketch="$(BUILD)/SelsortTest" --output="$(BUILD)/build" --force

Shellsort: build/ShellsortTest/success

build/ShellsortTest/success: Sorting/Shellsort.pde Sorting/SortTest.pde Utils/Swap.pde
	@echo "Shellsort Test"
	-@rm -rf build/ShellsortTest
	@mkdir build/ShellsortTest
	@cp Sorting/Shellsort.pde build/ShellsortTest
	@cp Utils/Swap.pde build/ShellsortTest
	@cp Sorting/SortTest.pde build/ShellsortTest/ShellsortTest.pde
	@$(PROCESS) --run --sketch="$(BUILD)/ShellsortTest" --output="$(BUILD)/build" --force

Mergesort: build/MergesortTest/success

build/MergesortTest/success: Sorting/Mergesort.pde Sorting/SortTest.pde Utils/Swap.pde Utils/Swap.pde
	@echo "Mergesort Test"
	-@rm -rf build/MergesortTest
	@mkdir build/MergesortTest
	@cp Sorting/Mergesort.pde build/MergesortTest
	@cp Utils/Swap.pde build/MergesortTest
	@cp Sorting/SortTest.pde build/MergesortTest/MergesortTest.pde
	@$(PROCESS) --run --sketch="$(BUILD)/MergesortTest" --output="$(BUILD)/build" --force

MergesortOpt: build/MergesortOptTest/success

build/MergesortOptTest/success: Sorting/MergesortOpt.pde Sorting/SortTest.pde Utils/Swap.pde
	@echo "MergesortOpt Test"
	-@rm -rf build/MergesortOptTest
	@mkdir build/MergesortOptTest
	@cp Sorting/MergesortOpt.pde build/MergesortOptTest
	@cp Utils/Swap.pde build/MergesortOptTest
	@cp Sorting/SortTest.pde build/MergesortOptTest/MergesortOptTest.pde
	@$(PROCESS) --run --sketch="$(BUILD)/MergesortOptTest" --output="$(BUILD)/build" --force

Quicksort: build/QuicksortTest/success

build/QuicksortTest/success: Sorting/Quicksort.pde Sorting/SortTest.pde Utils/Swap.pde Utils/Swap.pde
	@echo "Quicksort Test"
	-@rm -rf build/QuicksortTest
	@mkdir build/QuicksortTest
	@cp Sorting/Quicksort.pde build/QuicksortTest
	@cp Utils/Swap.pde build/QuicksortTest
	@cp Sorting/SortTest.pde build/QuicksortTest/QuicksortTest.pde
	@$(PROCESS) --run --sketch="$(BUILD)/QuicksortTest" --output="$(BUILD)/build" --force

Heapsort: build/HeapsortTest/success

build/HeapsortTest/success: Sorting/Heapsort.pde Sorting/SortTest.pde Trees/Maxheap.pde Utils/Swap.pde
	@echo "Heapsort Test"
	-@rm -rf build/HeapsortTest
	@mkdir build/HeapsortTest
	@cp Sorting/Heapsort.pde build/HeapsortTest
	@cp Sorting/SortTest.pde build/HeapsortTest/HeapsortTest.pde
	@cp Trees/Maxheap.pde build/HeapsortTest
	@cp Utils/Swap.pde build/HeapsortTest
	@$(PROCESS) --run --sketch="$(BUILD)/HeapsortTest" --output="$(BUILD)/build" --force

Binsort: build/Binsort/success

build/Binsort/success: Sorting/Binsort.pde Utils/Swap.pde Utils/Permute.pde
	@echo "Binsort Test"
	-@rm -rf build/Binsort
	@mkdir build/Binsort
	@cp Sorting/Binsort.pde build/Binsort
	@cp Utils/Swap.pde build/Binsort
	@cp Utils/Permute.pde build/Binsort
	@$(PROCESS) --run --sketch="$(BUILD)/Binsort" --output="$(BUILD)/build" --force


GraphDummy: build/GraphDummy/success

build/GraphDummy/success: Graphs/GraphDummy.pde Graphs/Graph.pde Graphs/GraphM.pde
	@echo "GraphDummy Test"
	-@rm -rf build/GraphDummy
	@mkdir build/GraphDummy
	@cp Graphs/GraphDummy.pde build/GraphDummy
	@cp Graphs/Graph.pde build/GraphDummy
	@cp Graphs/GraphM.pde build/GraphDummy
	@$(PROCESS) --run --sketch="$(BUILD)/GraphDummy" --output="$(BUILD)/build" --force

GraphTrav: build/GraphTrav/success

build/GraphTrav/success: Graphs/BFS.pde Graphs/DFS.pde Graphs/Graph.pde Graphs/GraphM.pde Graphs/GraphL.pde Graphs/GraphTrav.pde Graphs/GraphCreate.pde Lists/Queue.pde Lists/LQueue.pde Lists/Link.pde Graphs/GraphTrav.gph
	@echo "GraphTrav Test"
	-@rm -rf build/GraphTrav
	@mkdir build/GraphTrav
	@cp Graphs/GraphTrav.pde build/GraphTrav
	@cp Graphs/GraphTrav.gph build/GraphTrav
	@cp Graphs/GraphCreate.pde build/GraphTrav
	@cp Graphs/Graph.pde build/GraphTrav
	@cp Graphs/GraphM.pde build/GraphTrav
	@cp Graphs/GraphL.pde build/GraphTrav
	@cp Graphs/DFS.pde build/GraphTrav
	@cp Graphs/BFS.pde build/GraphTrav
	@cp Lists/Queue.pde build/GraphTrav
	@cp Lists/LQueue.pde build/GraphTrav
	@cp Lists/Link.pde build/GraphTrav
	@$(PROCESS) --run --sketch="$(BUILD)/GraphTrav" --output="$(BUILD)/build" --force

GraphTop: build/GraphTop/success

build/GraphTop/success: Graphs/TopsortBFS.pde Graphs/TopsortDFS.pde Graphs/Graph.pde Graphs/GraphM.pde Graphs/GraphL.pde Graphs/GraphTop.pde Graphs/GraphCreate.pde Lists/Queue.pde Lists/LQueue.pde Lists/Link.pde Graphs/GraphTop.gph
	@echo "GraphTop Test"
	-@rm -rf build/GraphTop
	@mkdir build/GraphTop
	@cp Graphs/GraphTop.pde build/GraphTop
	@cp Graphs/GraphTop.gph build/GraphTop
	@cp Graphs/GraphCreate.pde build/GraphTop
	@cp Graphs/Graph.pde build/GraphTop
	@cp Graphs/GraphM.pde build/GraphTop
	@cp Graphs/GraphL.pde build/GraphTop
	@cp Graphs/TopsortDFS.pde build/GraphTop
	@cp Graphs/TopsortBFS.pde build/GraphTop
	@cp Lists/Queue.pde build/GraphTop
	@cp Lists/LQueue.pde build/GraphTop
	@cp Lists/Link.pde build/GraphTop
	@$(PROCESS) --run --sketch="$(BUILD)/GraphTop" --output="$(BUILD)/build" --force

GraphDijk: build/GraphDijk/success

build/GraphDijk/success: Graphs/Graph.pde Graphs/GraphM.pde Graphs/GraphL.pde Graphs/GraphDijk.pde Graphs/GraphCreate.pde Lists/Queue.pde Lists/LQueue.pde Lists/Link.pde Graphs/GraphDijk.gph Graphs/Dijkstra.pde Graphs/DijkstraPQ.pde Utils/KVPair.pde Trees/MinheapKV.pde
	@echo "GraphDijk Test"
	-@rm -rf build/GraphDijk
	-@mkdir build/GraphDijk
	@cp Graphs/Graph.pde build/GraphDijk
	@cp Graphs/GraphM.pde build/GraphDijk
	@cp Graphs/GraphL.pde build/GraphDijk
	@cp Graphs/GraphDijk.pde build/GraphDijk
	@cp Graphs/GraphDijk.gph build/GraphDijk
	@cp Graphs/GraphCreate.pde build/GraphDijk
	@cp Lists/Queue.pde build/GraphDijk
	@cp Lists/LQueue.pde build/GraphDijk
	@cp Lists/Link.pde build/GraphDijk
	@cp Graphs/Dijkstra.pde build/GraphDijk
	@cp Graphs/DijkstraPQ.pde build/GraphDijk
	@cp Utils/KVPair.pde build/GraphDijk
	@cp Trees/MinheapKV.pde build/GraphDijk
	@$(PROCESS) --run --sketch="$(BUILD)/GraphDijk" --output="$(BUILD)/build" --force

GraphMCST: build/GraphMCST/success

build/GraphMCST/success: Graphs/Graph.pde Graphs/GraphM.pde Graphs/GraphL.pde Graphs/GraphMCST.pde Graphs/GraphCreate.pde Lists/Queue.pde Lists/LQueue.pde Lists/Link.pde Graphs/GraphTrav.gph Graphs/Prim.pde Graphs/PrimPQ.pde Graphs/Kruskal.pde Utils/KVPair.pde Trees/MinheapKV.pde
	@echo "GraphMCST Test"
	-@rm -rf build/GraphMCST
	@mkdir build/GraphMCST
	@cp Graphs/Graph.pde build/GraphMCST
	@cp Graphs/GraphM.pde build/GraphMCST
	@cp Graphs/GraphL.pde build/GraphMCST
	@cp Graphs/GraphMCST.pde build/GraphMCST
	@cp Graphs/GraphTrav.gph build/GraphMCST
	@cp Graphs/GraphCreate.pde build/GraphMCST
	@cp Lists/Queue.pde build/GraphMCST
	@cp Lists/LQueue.pde build/GraphMCST
	@cp Lists/Link.pde build/GraphMCST
	@cp Graphs/Prim.pde build/GraphMCST
	@cp Graphs/PrimPQ.pde build/GraphMCST
	@cp Graphs/Kruskal.pde build/GraphMCST
	@cp Utils/KVPair.pde build/GraphMCST
	@cp Trees/MinheapKV.pde build/GraphMCST
	@cp Trees/ParPtrTree.pde build/GraphMCST
	@$(PROCESS) --run --sketch="$(BUILD)/GraphMCST" --output="$(BUILD)/build" --force