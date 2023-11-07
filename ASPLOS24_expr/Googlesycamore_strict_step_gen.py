import sys

def main(argv):
    idx = argv[1]
    out_str = '''
    // Step ''' + str(idx) + \
    '''
    void SWAP_''' + str(idx) + '''(ref int[6][2] pos) {
        int beg_u = ??;
        int end_u = ??;
        int beg_d = ??;
        int end_d = ??;
        for (int k = beg_u; k < end_u; k += 2) {
            int tmp = pos[0][k];
            pos[0][k] = pos[0][k + 1];
            pos[0][k + 1] = tmp;
        }
        for (int k = beg_d; k < end_d; k += 2) {
            int tmp = pos[1][k];
            pos[1][k] = pos[1][k + 1];
            pos[1][k + 1] = tmp;
        }
    }

    void CPHASE_''' + str(idx) + '''(ref int[6][6] I, ref int[6][2] pos) {
        int beg_u = ??;
        int end_u = ??;
        for (int k = beg_u; k < end_u; k+=2) {
            int small = pos[0][k];
            int big = pos[1][k-1] - 6;
            assert(I[small][big] == 0);
            for (int p = 0; p < small; p++) {
                assert(I[p][big] == 1);
            }
            I[small][big] = 1;
        }
    }

    void step_'''+str(idx)+'''(ref int[6][6] I, ref int[6][2] pos) {
    int flag = ??(1);
        if (flag == 0) {
            SWAP_'''+str(idx)+'''(pos);
        } else {
            CPHASE_'''+str(idx)+'''(I, pos);
        }
    }'''
    print(out_str)
if __name__ == '__main__':
    main(sys.argv)
