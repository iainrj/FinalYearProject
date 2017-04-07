import { h, Component } from 'preact';
import style from './style';

export default function (props) {
	const transform = `translate(0, ${props.index * props.padding})`;
	const width = `${props.xScale(props.score) + 10}px`;
	const x = props.xScale(props.score);
	return (
		<g transform={transform}>
			<rect class={style.chart_rect} width={width} height="20"></rect>
			<text class={style.chart_text} x={x} y="9.5" dy=".35em">{props.score}</text>
		</g>
	);
}
