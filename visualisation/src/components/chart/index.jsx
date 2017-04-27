import { h, Component } from 'preact';
import BarPlot from '../bar-plot';
import ScoreBoard from './scoreboard';

const styles = {
	width   : 1200,
	height  : 800,
	padding : 25
};

export default class Chart extends Component {
	constructor() {
		super();

		this.state.data = {data: ScoreBoard};
	}

	render() {
		return (
			<BarPlot round={this.props.round} {...this.state} {...styles}/>
		);
	}
}
