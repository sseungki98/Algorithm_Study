# [Gold V] 줄서기 - 17178 

[문제 링크](https://www.acmicpc.net/problem/17178) 

### 성능 요약

메모리: 34200 KB, 시간: 68 ms

### 분류

자료 구조, 구현, 시뮬레이션, 스택

### 제출 일자

2023년 10월 10일 00:44:48

### 문제 설명

<p>아이즈원의 팬인 시온이는 드디어 티켓팅에 성공하여 콘서트를 갔다. 콘서트장에 일찍 도착한 시온이는 기대하며 입장을 위해 줄을 섰다. 하지만 아이즈원의 인기대로 시온이를 포함한 많은 팬이 줄을 서고 있다. 콘서트의 입장이 시작되었고 입장은 티켓 번호 순서대로 이루어졌다. 하지만 입구에 너무 많은 팬이 몰려 아무도 이동할 수 없는 상황이 되었고, 결국 주최 측에서 인원을 정렬시켜 다음과 같이 간신히 사람 한 줄이 설 수 있는 대기 공간을 만들었다.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/bc504cb9-71fa-4df1-8ad9-0575a0203262/-/preview/"></p>

<p>주최 측은 번호표 순서대로만 통과할 수 있는 입구를 만들어 두었지만, 줄에서는 마구잡이로 사람들이 기다리고 있다. 대기 공간을 이용하여 입장이 원활히 이루어지도록 하려고 한다. 콘서트장에 사람들이 제대로 들어갈 수 있는지 확인해보자.</p>

<p>사람들은 현재 5명씩 <em>N </em>줄을 서 있고, 첫 번째 줄 맨 앞사람만 이동이 가능하다. 이 사람은 콘서트장으로 입장할 수도 있고 대기 공간에서 다시 기다릴 수도 있다. 한 줄의 사람이 다 이동했다면 그다음 줄의 사람들이 이동한다. 대기 공간에는 한 줄로만 설 수 있는 공간이 있으며, 마지막에 들어온 사람부터 나갈 수 있다. 나갈 경우 바로 입장해야 하고, 다시 줄로 돌아갈 수는 없다. 티켓은 A-123과 같이 한 개의 대문자 알파벳과 '-', 1000 미만의 자연수의 조합으로 이뤄어져 있다. 만약 수가 7이라면 A-7과 같이 주어진다. 티켓의 순서는 알파벳이 빠른 티켓이 빠르며, 동일하다면 더 적은 수가 더 빠르다. 티켓 번호는 중복되게 주어지지 않는다.</p>

<p>위의 예시를 예로 들면 다음과 같이 모든 사람들이 입장할 수 있다. 그림과는 달리 대기 공간에는 무한히 많은 사람들이 들어올 수 있다는 것에 주의하여야 한다.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/9827f814-14b0-4334-8af0-10a89be7a623/-/preview/"></p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/d21ef9b6-6de8-4640-8822-b142f4cccf6c/-/preview/"></p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/8af4d04f-6fa2-40d4-ad4c-d21cd50f8389/-/preview/"></p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/6ce1200a-d930-4d6a-9a45-f785857737b8/-/preview/"></p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/828c1fd8-a5d8-4728-980a-f7371db21328/-/preview/"></p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/aa24fa18-f5cb-4a1c-9fd7-e88c38bd1c31/-/preview/"></p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/4433b135-81c3-4b12-9431-e761c71dd6cd/-/preview/"></p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/052561a8-730e-43ab-b929-2ebe0d6ff31d/-/preview/"></p>

### 입력 

 <p>첫째 줄에는 줄에서 기다리고 있는 사람들의 줄 수 <em>N</em>이 주어진다. (1 ≤ <em>N</em> ≤ 100)</p>

<p>둘째 줄부터 <em>N </em>개의 줄에는 한 줄에 서 있는 5명의 티켓 번호가 주어진다.</p>

<p>사람들이 서 있는 순서대로 입력이 주어진다.</p>

### 출력 

 <p>모든 사람이 무사히 콘서트장에 입장할 수 있다면 “GOOD”을 출력하고 그렇지 않다면 “BAD”를 출력한다.</p>

