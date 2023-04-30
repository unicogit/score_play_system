a=[['1','2','3'],['4','5']]
b=['1','2','3','4','5']
for i in range(len(a)):
    for j in range(len(a[i])):
        print(f'探索{i}',end = '¥n')
        print('探索元'+a[i][j])
        for k in range(len(b)):
            if (b[k]==a[i][j]):
                print('b:'+b[k])
                break


