##########OpenSource_project###########

## 변수(각각 형용사, 동사1,2, 명사1,2, 장소, 이름 ) 에 키보드로 부터 입력받기 
#adj = input('Adjective: ')
#verb1 = input('Verb: ')
#verb2 = input('Verb: ')
#noun1 = input('Noun: ')
#place = input('Place: ')
#noun2 = input('Noun: ')
#name = input('Name: ')

## 매드립 변수에 f스트링 저장
## f스트링에 문장과 앞서 입력한 단어 조합
#madlib = f'Computer science is {adj}. I can {verb1} while sitting on a {noun2} #and {verb2}. I once went to the {place} and found a big {noun1}! I decided that would be a great place for {name}.'

## 매드립 출력
#print(madlib)

#############################원본 소스 코드 카피#############################



# def함수로 묶어줍니다.
def madlip():

    # 프로그램 시작을 알리고, 선택하라고 명시합니다.

    print('madlip 프로그램을 시작합니다!')
    print('1/2/3/4/5/6 중 한개를 선택하세요!')
    print('1~3은 영어, 4~6은 한국어 입니다!')

    # choice 변수를 선언하고, input으로 입력받습니다.
    choice = input('선택 : ')

    # 만약, 1~6이 아닌 숫자를 입력한다면 오류로서 종료합니다.
    if choice not in ['1','2','3','4','5','6']:
     print('잘못된 선택입니다. 종료합니다ㅠㅠ')
     return

    # 단어변수를 입력을 받습니다.
    sub = input('주어를 입력하세요 : ')
    verb1 = input('첫번째 동사를 입력하세요 : ')
    verb2 = input('두번째 동사를 입력하세요 : ')
    pla = input('장소를 입력하세요 : ')
    abj = input('형용사를 입력하세요 : ')
    noun1 = input ('첫번째 명사를 입력하세요 :')
    noun2 = input ('두번째 명사를 입력하세요 : ')


    # 고른 번호대로 각각 madlip변수에 f스트링을 이용해서 삽입, 미리 만든 문장과 조합 합니다. 1~3은 영어, 4~6은 한국어 입니다.
    if choice == '1':
        madlip = f'{sub} {verb1}(s/ed) a {noun1} in {pla} but, {sub} {verb2} {abj} {noun2} '
    elif choice == '2':
        madlip = f'{sub} was {verb1}ing and then {verb2}ing at {pla} when {sub} found {abj} {noun1} and {noun2}'
    elif choice == '3':
        madlip = f'A {abj} {noun1} appeared to {sub}, {verb1}ed and {verb2}ed, and left {pla}. {noun2} followed them.'
    elif choice == '4':
        madlip = f'{sub}는 {pla}에서  {noun1} 을/를 {verb1} 하지만, {sub}는 {abj} {noun2}가 {verb2}'
    elif choice == '5':
        madlip = f'{sub}는 {pla}에서 {noun2}를 보고 깜짝 놀랐다. 그 이유는 {abj} {noun1}이/가  {verb1}하고 있었기 때문이다.'
    elif choice == '6':
        madlip = f'{verb1}을 잘하던 {sub}는  {pla}에서 {abj} {noun2}를 만났고, {verb2}하면서 친해졌다.'

    # print함수로 출력합니다
    print('\n결과는...?\n')
    print(madlip)
    print('수고하셨습니다!')

#def함수로 지정해준 madlip 함수를 실행합니다.
madlip()



