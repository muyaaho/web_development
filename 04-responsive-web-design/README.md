## Comparing Units (specifically for font-size)
| px                                 | %                               | em  | rem    |
| ---------------------------------- | ------------------------------- | --- | --- |
| Easy to understand & translateable | Relatice to parent element size | Size is relative to font-size -> 속성이 중요하기 때문, 폰트 크기는 부모의 요소와 관련됨    | Size is relative to root element's font size -> 최상위 요소(html)폰트 크기와 관련    |
| Limited user focus & not scalable  | Hard to manage due to cascading nature                                | Hard to manage due to cascading nature     | Preferred choice if applicable    |


- 픽셀: 적응형 디자인

- 모바일에서 보기 위해서는 좀 더 동적인 유닛이 필요함 -> %, em, rem