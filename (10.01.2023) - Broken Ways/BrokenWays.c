#include <stdio.h>
#include <stdbool.h>

#define MOD 1000000007

int num_ways(int n, int m, int broken_steps[m])
{
    bool is_broken[n + 1];
    for (int i = 0; i <= n; i++)
    {
        is_broken[i] = false;
    }
    for (int i = 0; i < m; i++)
    {
        is_broken[broken_steps[i]] = true;
    }

    int dp[n + 1];
    dp[0] = 1;
    for (int i = 1; i <= n; i++)
    {
        dp[i] = 0;
        if (!is_broken[i])
        {
            dp[i] = dp[i - 1];
        }
        if (!is_broken[i] && i > 1 && !is_broken[i - 2])
        {
            dp[i] = (dp[i] + dp[i - 2]) % MOD;
        }
    }
    return dp[n];
}

int main()
{
    int n, m;
    scanf("%d%d", &n, &m);
    int broken_steps[m];
    for (int i = 0; i < m; i++)
    {
        scanf("%d", &broken_steps[i]);
    }
    printf("%d", num_ways(n, m, broken_steps));
    return 0;
}