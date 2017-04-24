import { h, Component } from 'preact';
import style from './style';

export default class Bar extends Component {
	constructor() {
		super();

		this.state.score = 0;
	}

	componentWillReceiveProps(nextProps) {
		console.log(nextProps.newScore);
		this.setState({score: this.state.score + nextProps.newScore});
	}

	componentWillUnmount() {
		this.setState({score: 0});
	}

	render() {
		const transform = `translate(0, ${this.props.id * this.props.padding})`;
		const width = `${this.props.xScale(this.state.score) + 10}`;
		return (
			<g class={style.bar_bar} transform={transform}>
				<rect class={style.chart_rect} width={width} height="20"></rect>
				<text class={style.chart_text} x={width - 5} y="9.5" dy=".35em">{this.state.score}</text>
				{/*<text class={style.chart_text} x={} y="9.5" dy=".35em">{this.props.countryName}</text>*/}
			</g>
		);
	}
}
