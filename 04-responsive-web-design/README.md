## Comparing Units (specifically for font-size)
| px                                 | %                               | em  | rem    |
| ---------------------------------- | ------------------------------- | --- | --- |
| Easy to understand & translateable | Relatice to parent element size | Size is relative to font-size -> 속성이 중요하기 때문, 폰트 크기는 부모의 요소와 관련됨    | Size is relative to root element's font size -> 최상위 요소(html)폰트 크기와 관련    |
| Limited user focus & not scalable  | Hard to manage due to cascading nature                                | Hard to manage due to cascading nature     | Preferred choice if applicable    |


- 픽셀: 적응형 디자인

- 모바일에서 보기 위해서는 좀 더 동적인 유닛이 필요함 -> %, em, rem

- 브라우저 기본값으로 설정됨, 그런데 food-item-content에 설정된다면 h2의 부모값이 food-item-content이므로 food-item-content와 같게 만들어짐 
- 1em == 100% 
- rem은 브라우저 기본값의 배수(2rem == 2 * 16px)

- padding의 %는 부모요소의 %로됨
- 하지만 padding에 em, rem은 font-size의 배수로 결정됨!

#### Note
항상 정답은 아님. 개인 선호도나 프로젝트 요구 사항에 따라 Unit을 선택해야됨

