def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        d = {}
        for domain in cpdomains:
            n, dname = domain.split(" ")
            if dname not in d:
                d[dname] = int(n)
            else:
                d[dname] += int(n)
            
            for sdi in range(len(dname)):
                if dname[sdi] == ".":
                    if dname[sdi+1:] not in d:
                        d[dname[sdi+1:]] = int(n)
                    else:
                        d[dname[sdi+1:]] += int(n)
        
        res = []
        for k, v in d.items():
            res.append(str(v) + " " + k)
        return res
