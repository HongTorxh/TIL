def solution(s):
    answer = ''
    count = 0
    while count < len(s) :
        if s[count].isdigit():
            answer += s[count]
            count += 1
        else:
            if s[count] == 'z':
                answer += '0'
                count = count + 4
            elif s[count] == 'o':
                answer += '1'
                count = count + 3

            elif s[count] == 't':
                if s[count+1] == 'w':
                    answer += '2'
                    count+=3
                else:
                    answer += '3'
                    count+=5
            elif s[count] == 'f':
                if s[count+1] == 'o':
                    answer += '4'
                    count+=4
                else:
                    answer += '5'
                    count+=4
            elif s[count] == 's':
                if s[count+1] =='i':
                    answer += '6'
                    count+=3
                else:
                    answer += '7'
                    count+=5
            elif s[count] == 'e':
                answer += '8'
                count+=5
            elif s[count] == 'n':
                answer += '9'
                count+=4
    answer = int(answer)
    return answer
