# https://leetcode.com/problems/unique-email-addresses/

class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        count = 0
        unique = set()
        for email in emails:
            local, domain = email.split('@')
            unique_local = local.replace('.', '').split('+')[0]
            unique_email = unique_local + '@' + domain
            unique.add(unique_email)
        # print(unique)
        return len(unique)
            


