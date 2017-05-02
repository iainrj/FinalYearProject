import { h, Component } from 'preact';
import { scaleLinear } from 'd3-scale';
import Bar from '../bar';

const performers = ['Ukraine','Belarus','Azerbaijan','Iceland','Norway','Romania','Armenia','Montenegro','Poland','Greece','Austria', 'Germany','Sweden','France','Russia','Italy','Slovenia','Finland','Spain','Switzerland','Hungary','Malta','Denmark','The Netherlands', 'San Marino','United Kingdom'];

const voters = ['Albania', 'Armenia', 'Austria', 'Azerbaijan', 'Belarus', 'Belgium', 'Denmark', 'Estonia', 'FYR Macedonia', 'Finland', 'France','Georgia', 'Germany', 'Greece', 'Hungary', 'Iceland', 'Ireland', 'Israel', 'Italy', 'Latvia', 'Lithuania', 'Malta', 'Moldova', 'Montenegro', 'Norway', 'Poland', 'Portugal', 'Romania', 'Russia', 'San Marino', 'Slovenia', 'Spain', 'Sweden', 'Switzerland', 'The Netherlands', 'Ukraine', 'United Kingdom'];

// const bad_reveal_order = ['Azerbaijan','Greece','Poland','Albania','San Marino','Denmark','Montenegro','Romania','Russia','The Netherlands','Malta','France','United Kingdom','Latvia','Armenia','Iceland','FYR Macedonia','Sweden','Belarus','Germany','Israel','Portugal','Norway','Estonia','Hungary','Moldova','Ireland','Finland','Lithuania','Austria','Spain','Belgium','Italy','Ukraine','Switzerland','Georgia','Slovenia'];
const good_reveal_order = ['Belarus', 'Albania', 'Poland', 'United Kingdom', 'Montenegro', 'Armenia', 'Malta', 'Russia', 'Azerbaijan', 'Germany', 'San Marino', 'Italy', 'FYR Macedonia', 'Moldova', 'Estonia', 'Austria', 'Romania', 'Switzerland', 'Ukraine', 'Latvia', 'Denmark', 'Georgia', 'Hungary', 'Finland', 'Ireland', 'Norway', 'Greece', 'Spain', 'Israel', 'Portugal', 'Lithuania', 'France', 'Belgium', 'Iceland', 'Sweden', 'Slovenia', 'The Netherlands'];

let reveal_order = good_reveal_order;

export default class BarPlot extends Component {
	constructor() {
		super();

		this.state.cumScores = new Array(26).fill(0);
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

						const country_index = reveal_order[this.props.round - 1];
						const score = country_scores[voters.indexOf(country_index)];

						const topScore = this.getTopScore(score, c);

						const countryProps = {
							countryName: country,
							id: index,
							round: this.props.round - 1,
							newScore: score,
							padding: this.props.padding,
							xScale: this.xScale,
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
