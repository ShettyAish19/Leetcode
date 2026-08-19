class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        mail_to_name={}

        par={}
        size={}

        def find(x):
            if x==par[x]:
                return x

            par[x]=find(par[x])
            return par[x]

        def union(x,y):
            a,b=find(x),find(y)
            if a==b:
                return
            if size[b]>size[a]:
                a,b=b,a

            par[b]=a
            size[a]+=size[b]

            
        for account in accounts:
            name=account[0]
            first=account[1]

            for email in account[1:]:
                if email not in par:
                    mail_to_name[email]=name
                    par[email]=email
                    size[email]=1
                union(first,email)

        groups={}

        for email in par:
            root=find(email)

            if root in groups:
                groups[root].append(email)

            else:
                groups[root]=[email]

        res=[]
        for root,emails in groups.items():
            emails.sort()
            
            res.append([mail_to_name[root]] + emails)

        return res
        


        

        