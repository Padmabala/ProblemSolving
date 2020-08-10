
def splitArray(nums,m):
        n = len(nums)
        #f[][] = new int[n + 1][m + 1];
        #sub[] = new int[n + 1];
        f=[[float("inf") for i in range(m+1)]for i in range(n+1)]
        sub=[0 for i in range(n+1)]
        print(f)
        print(sub)
        # for (int i = 0; i <= n; i++) {
        #     for (int j = 0; j <= m; j++) {
        #         f[i][j] = Integer.MAX_VALUE;
        #     }
        # }
        for i in range(n):
            sub[i+1]=sub[i]+nums[i]
        print(sub)
        # for (int i = 0; i < n; i++) {
        #     sub[i + 1] = sub[i] + nums[i];
        # }
        f[0][0] = 0;
        for i in range(1,n+1):
            for j in range(1,m+1):
                for k in range(0,i):
                    print("i,j,k",i,j,k)
                    print("f[i][j]=>f[",i,"][",j,"]",f[i][j]);
                    print("f[k][j - 1]=>f[",k,"][",j-1,"]",f[k][j - 1])
                    print("sub[i] - sub[k]=>sub[",i,"]-sub[",j,"]",sub[i],"-",sub[k],"==>",sub[i] - sub[k])
                    print("min(",f[i][j], ",max(",f[k][j - 1],",", sub[i] - sub[k],"))")
                    f[i][j] = min(f[i][j], max(f[k][j - 1], sub[i] - sub[k]))
        print(f)
        #         while(k<i){
        #             f[i][j] = Math.min(f[i][j], Math.max(f[k][j - 1], sub[i] - sub[k]));
        #         }
        # for (int i = 1; i <= n; i++) {
        #     for (int j = 1; j <= m; j++) {
        #         for (int k = 0; k < i; k++) {
        #             f[i][j] = Math.min(f[i][j], Math.max(f[k][j - 1], sub[i] - sub[k]));
        #         }
        #     }
        # }
        return f[n][m];
splitArray([7,2,5,10,8],2)

