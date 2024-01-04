## Content
- Project Example: Tips & Tricks to Create Beautiful Websites
- CSS Custom Properties, Transitions & SVG Basics

## 3 Things to Remember
1. Add **different features** step-by-step
2. Think about the **core information** that should be transferred
3. Less is more - **Don't over your website**

## More About Selectors
- html
	- Selects html element(= root element of an html file)
	- CSS rules are applied to html element & inherited to nested elements inside the html element
- :root(pseudo-selector)
	- Selects element which is the root of the document
	- CSS rules are applied to root element & inherited to nested elements inside the root element
	- root 가 html보다 높음
- `*`
	- Selects all elements of the html document
	- CSS rules are applied to all elements(specificity must be considered though)

## CSS Transformations & Transitions
- Transformation (변환)
	- 요소의 모양을 이동하거나 변경
- Transition (전환)
	- 초기 상태에서 부드럽게 전환
	- 변환할 때 전환을 통해 부드럽게 변화시킴

## CSS Transition
```CSS
transition: transform 0.5s ease-out 1s;
transition: {속성} {지속시간} {타이밍 기능timing function} {delay 전환이 바로실행될지 지연시간 있을지}
```
- 전환을 촉발하는 이벤트가 아니라 전환 초기에 적용됨

```CSS
.card-container {
  background-color: rgb(255, 255, 255);
  width: 350px;
  margin: 50px auto;
  box-shadow: 3px 3px 10px rgb(201, 200, 200);
  transition: background-color 0.5s ease-out;
}

.card-container:hover {
  /* transform: scale(1.05); */
  background-color: yellow;
}
```
- 이런 식으로 hover에 적용하려면 hover의 부모에 transition 정의, hover에는 바뀌는 변환 내용(transform)을 정의해야됨