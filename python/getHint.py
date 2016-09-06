# coding:utf-8


class Solution(object):

    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        right = 0
        wrong = 0
        rewrite_secret = [ v for v in secret]
        rewrite_guess = [ v for v in guess]
        if len(secret) != len(guess):
            return None
        for index, v in enumerate(secret):
            if guess[index] == v:
                right += 1
                rewrite_secret[index] = '*'
                rewrite_guess[index] = '*'
                continue

        for index, v in enumerate(rewrite_guess):
            if rewrite_guess[index] == "*":
                continue
            try:
                j = rewrite_secret.index(v)
                rewrite_secret[j]="*"
                wrong += 1
            except:
                continue
        return '%sA%sB'%(right, wrong)

def main():
    # 测试用例很重要
    a = Solution()
    print a.getHint("1807","7810")
    print a.getHint("11","11")
    print a.getHint("1234","0111")


if __name__ == "__main__":
    main()
