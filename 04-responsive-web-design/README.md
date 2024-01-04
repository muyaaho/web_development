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

## What about responsive design?
어떻게 장치마다 웹사이트를 다 보여줄 수 있을까?

### Desktop First vs Mobile First
설계할 때 어느 기기를 초점으로 맞추는가? Desktop First는 데스트탑을 기준으로 웹 페이지를 디자인 한 후 크기가 작아졌을 때 잘 보이게 만듬

| Desktop | Mobile |
| ---- | ---- |
| 전통적인 접근 방식 | 기능적인 접근 방식(크기 제한) |
| 사무실 기반 고객에 집중 | 라이프스타일/뉴스에 집중 |
| 기능이 많은 웹사이트를 만들 수 있음 | 컨텐츠 우선 |


## Getting started with Media Queries
```CSS
@media (min-width or max-width: 1200px){
	p{font-size: 2rem;}
}
```
반응형 웹사이트는 미디어 쿼리로 구현할 수 있음
- 미디어 쿼리는 CSS 코드임
- 미디어 유형에 대한 정보 수집(장치 유형, 사양 정보)
- 장치 유형이 기준에 적합하다면 미디어 쿼리 안의 코드가 실행됨
- 미디어 쿼리가 실행되면 변경이 아닌 속성이 추가됨
코드 설명
- 장치의 너비나 높이가 1200px 이상이면 코드 실행
- max-width: Desktop First
- min-width: Mobile First

## Common Breakpoints for Media Queries
- Portrait
	- Smartphon: 480px
	- Tablet: 768px
- Landscape
	- Notebook: 1024px
	- Desktop Computer: 1200px
	- TV: > 1200px


## Hamburger Icon & Side Drawer
1. Create clickable hamburger button in mobile view (모바일 뷰에만 보임)
2. Open side drawer on first button blick
		![[Pasted image 20240104135744.png]]
3. Close side drawer on second button click

## New Topics Covered
- Internal links
	- Adds defined ID to URL
	- href="#id"
- The target selector
	- Activates CSS rules if defined ID is selected in URL
	- #id: target

## 완성
- 데스크탑

  ![image](https://github.com/muyaaho/web_development/assets/76798969/76f56442-a06b-4b95-8ccb-919f5e4f04cd)

- 모바일

  ![image](https://github.com/muyaaho/web_development/assets/76798969/524a79bd-6b0d-42f2-9a49-958fa4b3d5f1) | ![image](https://github.com/muyaaho/web_development/assets/76798969/5f734e82-2b4c-4276-ac15-a86f686b6b2c)
  --- | --- |

## 정리
- px 대신 사용자 글자 크기에 따른 rem, em이라는 단위도 있다. 보통 rem을 많이 사용함(정답은 아님)
- media query를 통해 너비 별로 나타나는 화면을 바꿀 수 있음 -> 반응형
