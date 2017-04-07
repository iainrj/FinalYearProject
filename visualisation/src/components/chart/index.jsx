import { h, Component } from 'preact';
import BarPlot from '../bar-plot';
import ScoreBoard from './scoreboard';

const styles = {
	width   : 1000,
	height  : 1000,
	padding : 30
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
