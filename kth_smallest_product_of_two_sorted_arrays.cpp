/*
Given two sorted 0-indexed integer arrays nums1 and nums2 as well as an integer k, return the kth (1-based) smallest product of nums1[i] * nums2[j] where 0 <= i < nums1.length and 0 <= j < nums2.length.
*/
class Solution {

public:
  long long kthSmallestProduct(vector<int> &nums1, vector<int> &nums2,
                               long long k) {
    int a = max(abs(nums1[0]), abs(nums1[nums1.size() - 1]));
    int b = max(abs(nums2[0]), abs(nums2[nums2.size() - 1]));
    long long r = 1LL * a * b;
    long long l = -r;
    while (l < r) {
      long long mid = (l + r) >> 1;
      if (calculate(mid, nums1, nums2) >= k) {
        r = mid;
      } else {
        l = mid + 1;
      }
    }
    return l;
  }

private:
  long long calculate(long long p, vector<int> &nums1, vector<int> &nums2) {
    long long cnt = 0;
    for (int x : nums1) {
      if (x > 0) {
        int l = 0;
        int r = nums2.size();
        while (l < r) {
          int mid = (l + r) >> 1;
          if (1LL * x * nums2[mid] > p) {
            r = mid;
          } else {
            l = mid + 1;
          }
        }
        cnt += l;
      } else if (x < 0) {
        int l = 0;
        int r = nums2.size();
        while (l < r) {
          int mid = (l + r) >> 1;
          if (1LL * x * nums2[mid] <= p) {
            r = mid;
          } else {
            l = mid + 1;
          }
        }
        cnt += nums2.size() - l;
      } else if (p >= 0) {
        cnt += nums2.size();
      }
    }
    return cnt;
  }

};
