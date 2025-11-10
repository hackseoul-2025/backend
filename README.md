<img src="https://github.com/user-attachments/assets/76b75374-7c02-4341-9e46-5e7669641f8a" />

<div align="center">
    <h3>프레임을 넘어, 당신의 세계로</h3>
    <p>박물관의 걸작을 내 손 안의 도슨트로 만들어주는 <b>"뭐지엄(Whatisum)"</b> 입니다.</p>
</div>

## 🗿 Team Whatisum

<div>
  <div align="center">
    <table>
      <tr>
        <th>김수곤</th>
        <th>박정환</th>
        <th>유희진</th>
        <th>기태린</th>
      </tr>
      <tr>
        <td align="center">Leader, AI</td>
        <td align="center">FE</td>
        <td align="center">BE, DEVOPS</td>
        <td align="center">PM, DE</td>
      </tr>
      <tr>
        <td align="center"><a href="https://github.com/rocknroll17"/>@rocknroll17</a></td>
        <td align="center"><a href="https://github.com/19park"/>@19park</a></td>
        <td align="center"><a href="https://github.com/yu-heejin"/>@yu-heejin</a></td>
        <td align="center"><a href="https://github.com/xaerinoo"/>@xaerinoo</a></td>
      </tr>
    </table>
  </div>
</div>

## 🔎 Background

- **현재 박물관이 당면한 문제**
  
  - 낮은 디지털 참여율: 박물관 앱의 평균 이용률은 2.47%에 불과
    
  - 제한적인 Interaction: 기존 오디오 가이드나 텍스트 설명은 일방적이며 지루함
    
  - 젊은 세대의 박물관 이탈: 디지털 경험에 익숙한 Z세대는 전통적 박물관 방식에 흥미를 잃음


- **시장 상황**
  
  - 나날이 늘어나는 글로벌 박물관 기술 시장 규모: 2024년 62억$ → 2033년 174억$ (예상)
  - 게임 체인저로 작용하는 AR/VR 기술: 박물관 기술 시장의 선도적 기술 혁신으로, 2024년 기술 부문 매출의 30% 이상 차지
  - 모바일 AR이 문화유산 학습에 미치는 긍정적 영향
    
    - 78.21%의 지식 유지율
    - 사용도 만족도 및 몰입 경험 ↑

> #### Reference
> - [Museum App Statistics 2025: Why 90% of Native Apps Are Used by Less Than 3% of Visitors](https://www.nuseum.ai/en/museum-app-statistics-why-90-of-native-apps-fail/)
> - [Museum Technology Market Research Report 2033](https://marketintelo.com/report/museum-technology-market)
> - N. Xu, Y. Li, J. Lin, L. Yu and H. -N. Liang, "User Retention of Mobile Augmented Reality for Cultural Heritage Learning," 2022 IEEE International Symposium on Mixed and Augmented Reality Adjunct (ISMAR-Adjunct), Singapore, Singapore, 2022, pp. 447-452

## 💡 Our Solution

#### 뮤지엄? 뭐지엄?
- 관람객에게 직접 말을 거는 살아있는 페르소나
- 양방향 인터랙티브 대화
- 개인화된 스토리텔링과 감성적 연결

#### Business Model
- B2B2C 모델: 박물관과 계약 ⇒ 방문객에게 무료 서비스 제공
- 광고, 스폰서십

## 📱 UX Flow (MVP)

[Demo 영상 바로가기 🎬](https://www.youtube.com/shorts/INb94UmLhWc)

<img src="https://github.com/user-attachments/assets/ade75edc-f538-4ed3-a0f4-8c42ace85fa7" />

#### 현재 구현된 사항
- **5개 주요 작품**: 일반 LLM이 잘 다루지 못하는 작품에 집중
- **카메라 인식**: 실시간 작품 식별
- **2D 아바타 인터랙션**: TTS가 포함된 시각적 페르소나
- **채팅 히스토리**: 작품과의 과거 대화 내역

#### MVP 검증 목표
- 마이너한 작품에 대한 정보 전달 정확도 검증
- 페르소나 진정성에 대한 사용자 피드백 수집
- 파일럿 검증: 소규모 박물관과 파일럿 테스트 후 대형 박물관으로 확장

## ✅ Feature

#### 1. 카메라 기반 작품/유물 인식
- 컴퓨터 비전을 활용한 실시간 작품/유물 식별
- 스마트폰 카메라로 전시물을 비추고 클릭하면 즉시 대화 시작 가능

#### 2. 아바타 페르소나 + 음성(TTS)
- 각 작품이 고유한 성격을 가진 아바타로 변환
- 역사적 맥락을 생생하게 전달하는 자연스러운 음성 대화
- 의인화된 스토리텔링을 통한 감성적 연결
- 페르소나 별로 각각 다른 목소리

#### 3. RAG 기반 대화 엔진
- 큐레이션된 박물관 데이터베이스로부터 정확한 정보 제공
- 사용자 관심사에 맞춰 적응하는 자연스러운 대화 흐름
- 일반 LLM이 어려워하는 마이너한 작품/유물에 대한 전문 지식

#### 4. 직관적인 UX 플로우
- 간단한 사용자 여정: 작품 스캔 → 대화 → 채팅 기록 확인 → 다음 작품 스캔
- 박물관 환경에 최적화된 매끄러운 경험

## ⚙️ System Architecture

<img src="https://github.com/user-attachments/assets/1896dc69-e146-453c-bb10-feb09bc7bf12" />

- **Frontend**: Swift
- **Backend**: FastAPI
- **AI/ML pieline**: RAG, LLM, TTS, YOLO Fine tuning
- **Infra/DevOps**: AWS EC2, S3 bucket, RDS
- **GitHub Actions**: CI/CD

## 💻 Data Flow

```
사용자 카메라 → 이미지 인식 → 작품 식별 
    ↓
아바타 + 페르소나 로딩
    ↓
사용자 질문 → RAG 검색 → LLM 처리 → TTS
    ↓
자연스러운 음성 응답 + 텍스트 표시
```

## 🛤️ Roadmap

#### 2단계: 향상된 AR 경험
- **3D AR 아바타**: 증강 현실 속 전신 페르소나
- **아바타의 제스처**: 화면 속 아바타의 자연스러운 움직임
- **추천 질문 제공**

#### 3단계: 고급 인터랙션
- **향상된 상호작용**: 페르소나가 사용자에게 역질문
- **개인화된 투어**: 관심사 기반 박물관 탐색 경로 추천

#### 4단계: 플랫폼 확장
- **박물관 밖 문화유산**: 유적지
- **관광**: 도시 투어 및 관광명소
