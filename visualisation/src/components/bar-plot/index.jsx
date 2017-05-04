import { h, Component } from 'preact';
import { scaleLinear } from 'd3-scale';
import Bar from '../bar';

import {real, bad, good} from './orders';
import {voters, performers} from './comp';

export default class BarPlot extends Component {
	constructor() {
		super();

		this.state.cumScores = new Array(26).fill(0);
		this.state.revealOrder = good;
	}

	componentWillReceiveProps(nextProps) {
		let ord = good;

		if (nextProps.order === 'bad') {
			ord = bad;
		} else if (nextProps.order === 'real') {
			ord = real;
		}

		this.setState({revealOrder: ord});
	}

	updateCumulativeScores(score, index) {
		let newCumScores = this.state.cumScores;
		newCumScores[index] = newCumScores[index] + score;
		return newCumScores;
	}

	getTopScore(score = 0, index = 0) {
		const scores = this.updateCumulativeScores(score, index);
		let max = scores.reduce( (a, b) => {
			return Math.max(a, b);
		});
		return max;
	}

	render() {
		// Returns a function that "scales" X coordinates from the data to fit the chart
		const xScale = (props) => {
			return scaleLinear()
				.domain([0, 300])
				.range([15, 1000]);
		};
		const scales = { xScale: xScale() };

		return (
			<svg class="chart" width={this.props.width} height={this.props.height}>
				{
					performers.map((country, index) => {
						let country_scores = [];
						let c = performers.indexOf(country);

						for (let i = 0; i < voters.length; i++) {
							country_scores.push(this.props.data.data[c][i]);
						}

						const country_index = this.state.revealOrder[this.props.round - 1];
						const score = country_scores[voters.indexOf(country_index)] ? country_scores[voters.indexOf(country_index)] : 0;

						const topScore = this.getTopScore(score, c);

						const countryProps = {
							countryName: country,
							id: index,
							round: this.props.round - 1,
							newScore: score,
							padding: this.props.padding,
							highestScore: topScore
						};

						return (
							<Bar {...countryProps} {...scales} />
						);
					})
				}
			</svg>
		);
	}
}
