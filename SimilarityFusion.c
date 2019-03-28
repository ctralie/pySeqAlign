/*Programmer: Chris Tralie
*Purpose: To implement the fusion part of similarity network fusion*/
#include <stdio.h>
#include <stdlib.h>


/*
Ps: n_features x N x N array
Ss: n_features x N x N array
Js: n_features x N x K array of nearest neighbor indices
Pts: n_features x N x N array holding the current
estimate of the fused similarity matrices
nextPts: n_features x N x N array holding the staged fused similarity matrices at the end of an iteration
A: N x N array for temporary storage of the average similarity matrix in an iteration
*/
void snf(float* Ps, float* Ss, int* Js, float* Pts, float* nextPts, float* A, int n_features, int N, int K, int niters, float reg_diag) {
    float sum;
    int iter, i, j, k, l, feat, feat2, ni, nj;
    for (iter = 0; iter < niters; iter++) {
        for (feat = 0; feat < n_features; feat++) {
            for (i = 0; i < N; i++) {
                for (j = 0; j < N; j++) {
                    A[i*N+j] = 0.0;
                    nextPts[feat*N*N+i*N+j] = 0.0;
                }
            }
            // First take average of other features
            for (feat2 = 0; feat2 < n_features; feat2++) {
                if (feat2 == feat) {
                    continue;
                }
                for (i = 0; i < N; i++) {
                    for (j = 0; j < N; j++) {
                        A[i*N+j*N] += Pts[feat2*N*N+i*N+j*N]/(n_features-1);
                    }
                }
            }
            // Now perform the random walk for each feature type
            for (feat2 = 0; feat2 < n_features; feat2++)
            {
                if (feat2 == feat) {
                    continue;
                }
                for (i = 0; i < N; i++) {
                    for (j = 0; j < N; j++) {
                        sum = 0.0;
                        // For k in Ni
                        for (k = 0; k < K; k++) {
                            ni = Js[feat*N*K+i*K+k];
                            // For l in Nj
                            for (l = 0; l < K; l++) {
                                nj = Js[feat*N*K+j*K+l];
                                // S1(i,k)*S1(j,l)*P2(k,l)
                                nextPts[feat*N*N+i*N+j] += Ss[feat*N*N+i*N+ni]*Ss[feat*N*N+j*N+nj]*A[ni*N+nj];
                            }
                        }
                    }
                }
            }

        }

    }
}