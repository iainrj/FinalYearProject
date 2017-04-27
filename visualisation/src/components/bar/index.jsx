import { h, Component } from 'preact';
import style from './style';

export default class Bar extends Component {
	constructor() {
		super();

		this.state.score = 0;
	}

	componentWillReceiveProps(nextProps) {
		this.setState({score: this.state.score + nextProps.newScore});
	}

	componentWillUnmount() {
		this.setState({score: 0});
	}

	render() {
		const transformBar = `translate(0, ${this.props.id * this.props.padding})`;
		const width = `${+this.props.xScale(this.state.score) + 10}`;
		const transformName = `translate(${+width+5}, ${this.props.id * this.props.padding})`;
		return (
			<g>
				<g transform={transformBar}>
					<rect class={style.chart_rect} width={width} height="20"></rect>
					<text class={style.chart_text} x={width - 5} y="9.5" dy=".35em">{this.state.score}</text>
				</g>
				<g transform={transformName}>
					<text class={style.chart_text__country} x={0} y="9.5" dy=".35em">{this.props.countryName}</text>
				</g>
			</g>
		);
	}
}
