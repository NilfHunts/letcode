class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, max_length, char_set = 0, 0, set()
        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)
        return max_length
