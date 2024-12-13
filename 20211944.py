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

###################################코드 카피#############################

# 프로그램 시작을 알리고, 선택하라고 명시합니다.
print('madlip 프로그램을 시작합니다!')
print('1/2/3/4/5/6 중 한개를 선택하세요!')

# choice 변수를 선언하고, input으로 입력받습니다.
choice = input('선택 : ')

#만약, 1~6이 아닌 숫자를 입력한다면 오류로서 종료합니다.
if choice not in ['1','2','3','4','5','6']:
    print('잘못된 선택입니다. 종료합니다ㅠㅠ')
    return





