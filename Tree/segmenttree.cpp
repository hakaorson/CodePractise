class segmentTree {
public:
	segmentTree(vector<int>& inputnums) :nums(inputnums) {
		initTree();
		//cout << "endl" << endl;
	}
	void initTree() {
        if (nums.size() == 0)return;
		int size = setTreeSize();
		for (int i = 0; i < size; i++)
			trees.push_back(0);
		buildTree(nums, trees, 0, 0, nums.size() - 1);
	}
	void buildTree(vector<int>& nums, vector<int>& tree, int node, int left, int right) {
		if (left == right) {
			tree[node] = nums[left];
			return;
		}
		int middle = (left + right) / 2;
		int leftChild = node * 2 + 1;
		int rightChild = node * 2 + 2;
		buildTree(nums, tree, leftChild, left, middle);
		buildTree(nums, tree, rightChild, middle + 1, right);
		tree[node] = tree[leftChild] + tree[rightChild];
		return;
	}
	int setTreeSize() {
		int size = static_cast<int>(nums.size())*2;
		int target = 1;
		while (size) {
			size = size >> 1;
			target *= 2;
		}
		return target;
	}
	int sumrange(int left, int right) {
		return sumrangeexplicet(left, right, 0, nums.size() - 1, 0);
	}

	int sumrangeexplicet(int left, int right, int leftbound, int rightbound, int cur) {

		if (left == leftbound && right == rightbound)return trees[cur];
		int result = 0;
		int middle = (leftbound + rightbound) / 2;
		if (left <=middle )
			result += sumrangeexplicet(left, min(middle,right), leftbound, middle, cur * 2 + 1);
		if (right>middle)
			result += sumrangeexplicet(max(left,middle+1), right, middle + 1, rightbound, cur * 2 + 2);
		return result;
	}
	void update(int index,int num){
		int sub = num - nums[index];
		nums[index] = num;
		updateintree(index, 0, nums.size() - 1, sub, 0);
	}

	void updateintree(int index, int left, int right, int sub, int cur) {
		trees[cur] += sub;
		if (left == right)
			return;
		int middle = (left + right) / 2;
		if (index > middle)updateintree(index, middle + 1, right, sub, cur * 2 + 2);
		else updateintree(index, left, middle, sub, cur * 2 + 1);
	}
private:
	vector<int> nums;
	vector<int> trees;
};

class NumArray {
public:
	NumArray(vector<int>& nums) :tree(nums){

	}

	void update(int i, int val) {
		tree.update(i, val);
	}

	int sumRange(int i, int j) {
		return tree.sumrange(i, j);
	}
private:
	segmentTree tree;
};