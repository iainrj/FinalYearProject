import { h, Component } from 'preact';
import { scaleLinear } from 'd3-scale';
import Bar from '../bar';

const performers = ['Ukraine','Belarus','Azerbaijan','Iceland','Norway','Romania','Armenia','Montenegro','Poland','Greece','Austria', 'Germany','Sweden','France','Russia','Italy','Slovenia','Finland','Spain','Switzerland','Hungary','Malta','Denmark','The Netherlands', 'San Marino','United Kingdom'];

const voters = ['Albania', 'Armenia', 'Austria', 'Azerbaijan', 'Belarus', 'Belgium', 'Denmark', 'Estonia', 'FYR Macedonia', 'Finland', 'France','Georgia', 'Germany', 'Greece', 'Hungary', 'Iceland', 'Ireland', 'Israel', 'Italy', 'Latvia', 'Lithuania', 'Malta', 'Moldova', 'Montenegro', 'Norway', 'Poland', 'Portugal', 'Romania', 'Russia', 'San Marino', 'Slovenia', 'Spain', 'Sweden', 'Switzerland', 'The Netherlands', 'Ukraine', 'United Kingdom'];

const reveal_order = ['Azerbaijan','Greece','Poland','Albania','San Marino','Denmark','Montenegro','Romania','Russia','The Netherlands','Malta','France','United Kingdom','Latvia','Armenia','Iceland','FYR Macedonia','Sweden','Belarus','Germany','Israel','Portugal','Norway','Estonia','Hungary','Moldova','Ireland','Finland','Lithuania','Austria','Spain','Belgium','Italy','Ukraine','Switzerland','Georgia','Slovenia'];
// Returns a function that "scales" X coordinates from the data to fit the chart
const xScale = (props) => {
	return scaleLinear()
		.domain([0, 300])
        .range([15, 1000]);
};

export default function (props) {
	const scales = { xScale: xScale() };
	// const scores = [0, 6, 1, 4, 0, 0, 10, 0, 7, 2, 20, 5, 19, 0, 4, 0, 0, 6, 7, 1, 3, 10, 3, 8, 0,0];
	const scores = [113, 43, 33, 58, 88, 72, 174, 37, 62, 35, 290, 39, 218, 2, 89, 33, 9, 72, 74, 64, 143, 32, 74, 238, 14, 40];

	return (
		<svg class="chart" width={props.width} height={props.height}>
			{
				performers.map((country, index) => {
					let country_scores = [];
					let c = performers.indexOf(country);

					for (let i = 0; i < voters.length; i++) {
						country_scores.push(props.data.data[c][i]);
					}

					const country_index = reveal_order[props.round];
					const score = country_scores[voters.indexOf(country_index)];

					const countryProps = {
						countryName: country,
						id: index,
						round: props.round,
						newScore: score,
						padding: props.padding,
						xScale: props.xScale
					};

					return (
						<Bar {...countryProps} {...scales} />
					);
				})
			}
		</svg>
	);
}
