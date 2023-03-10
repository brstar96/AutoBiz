# AutoBiz
귀찮은 반복 프로세스를 자동화해 시간을 아껴 주는 프로젝트

## Auto Slack Status Changer (WIP)
슬랙의 상태 메시지를 바꾸는 시간은 평균 "16.76초"가 소요됩니다. 응용 프로그램 목록에서 슬랙을 찾고, `🚌 근무중` 아이콘으로 바꾸고, `일정 시간 이후 제거`를 세팅하기까지 아무리 빨라도 10초입니다. </br>
하루에 10초씩 5일이면 50초, 4주면 3분이 소요됩니다. 2022년 기준 1년 근무일은 251일로, 한 사람당 총 41.83분을 이 단순한 작업에 사용하게 됩니다. 전 직원이 열명이라면 이 단순한 일에 6.97시간을 낭비하게 되죠. 

따라서 이 프로젝트에서는 Github Action을 활용해 슬랙 상태 메시지 변경을 자동화합니다. 이메일, 계정 정보와 같은 민감한 정보는 Git Repository Secrets에 담아 안전하게 보관합니다. 

## Auto Flexworktime-approval Request Submitter (Done!)
전문연구요원 및 산업기능요원의 관리규정에서는 다음과 같이 유연근무제에 대해 규정하고 있습니다. 

```
* 전문연구요원 및 산업기능요원의 관리규정([시행 2022. 12. 30.] 
[병무청훈령 제1908호, 2022. 12. 30., 일부개정]) 제 5장 복무관리 제 32조 
(연구요원 및 기능요원에 대한 복무관리)

7항에 따르면, 박사과정 전문연구요원을 제외한 연구요원과 기능요원은 1주 40시간 근로시간 선택형 유연근무를 실시 할 수 있다. 
사규ㆍ취업규칙 등에 유연근무를 규정하고 있고, 전자적 방식에 의해 주간(週間) 40시간 복무 여부를 확인 가능한 시스템을 갖춘 병역지정업체에 한정하여 유연근무를 실시할 수 있다. 
유연근무 시작일 전일까지 별지 제35호서식의 유연근무 신청(변경)서를 제출하여 병역지정업체장의 승인을 받아야 한다. 
```

따라서 사내 경영지원 직원에게 유연근무 시작 일주일 전 다음과 같은 문구로 결재를 상신해야 합니다. 


```
산업지원인력 유연근무제 운영지침에 따라 전문연구요원 유연근무제 실시시 사전승인을 실시해야 함. 

기간: 2023년 1월 30일 ~ 2023년 2월 3일 근무시간: 오전 7시 ~ 오후 4시
```

어쩔 수 없는 프로세스이지만, 900일 가까운 기간 동안 시행하는 것이 얼마나 귀찮고 소모적인지 굳이 이야기하지 않을게요. 이 프로젝트에서는 원티드스페이스 웹 페이지를 통해 유연근무 결제 프로세스를 다음과 같이 자동화합니다. 

![gif](./_assets/720p_30fps.gif)