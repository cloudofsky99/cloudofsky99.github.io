dynamic analysis as complementary solution

so we first proposed dynamic analysis tool
to complement to current methodology that has been tipped to static analysis for almost 10 years
once we have this tool we can revisit the results of previous static analysis solutions to help verify the food and even imporove on them with these two objectives in mind we designed a tool called dynamo
so dynamo builds on

그래서 우리는 거의 10년 동안 정적 분석으로 귀결된 현재의 방법론을 보완하기 위한 동적 분석 도구를 먼저 제안한다.
우리가 이 도구를 갖게 되면 우리는 이전의 정적 분석 솔루션의 결과를 재방문하여 음식을 검증하고 심지어 다이너모라고 불리는 이 두 가지 목표를 염두에 두고 그것들을 개선할 수 있다.
> 이전의 정적 분석 솔류션의 결과 재검토 가능

1. Complement the methodology
2. Revisit result of static analysis solutions



to detect the prmissions enforced by a specific API, we run a service that is unprivileged and called that API from the service.
if the API is protected with permissions it will consult the package manager service which acts as a central decision policy point to check if the caller has the required permission.

특정 API에 의해 강제된 사용 권한을 탐지하기 위해, 우리는 권한 없는 서비스를 실행하고 그 API를 서비스로부터 호출합니다.
API가 권한으로 보호되는 경우, 중앙 결정 정책 지점 역할을 하는 패키지 관리자 서비스와 상의하여 호출자가 필요한 권한을 가지고 있는지 확인합니다.


now to precisely caapture this permission check
we use a dynamic instrumentations framework called freedom which is used to insturment the target API and the permissio nchecking API from the package manager service such that they would report the stack traces call parameters and return value whenever they are called
so now when the testing service calls the target API gain the instrumented API
