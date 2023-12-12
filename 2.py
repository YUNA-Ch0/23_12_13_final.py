# Q.2 10점
# 모스부호 해독 프로그램 만들기
# 문자열 letter 가 매개변수로 주어질 때,
# letter 영어 소문자로 바꾼 문자열을 return 하는
# solution 함수를 완성하시오.
# 제한사항
# 1 ≤ letter 의 길이 ≤ 1,000
# letter 의 모스부호는 공백으로 나누어져 있습니다.
# letter 에 공백은 연속으로 두 개 이상 존재하지 않습니다.
# letter = 여러분의 좌우명 또는 인상 깊었던 말을 쓰시오.

def solution(letter):
    morse_code_dict = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'} 
    morse_code_list = letter.split(' ')
    #입력 모스 부호들을 공백 기준 리스트 변환
    answer = '' # return answer에 저장할 빈 문자열
    for code in morse_code_list: # 코드가 morse_code_dict에 있는지 확인
        if code in morse_code_dict:
            answer += morse_code_dict[code] 
            # morse_code_dict에 모스 부호에 맞는 영어 소문자를 
            # answer에 넣는다.
        else: 
            answer += code # 공백일때
    return answer # 영어 소문자로 바꾼 문자열을 return
# 실행
result = solution('.... --- -- . ... .-- . . - .... --- -- .')
print(result)