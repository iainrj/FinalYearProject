import { h, Component } from 'preact';
import { scaleLinear } from 'd3';
import Bar from '../bar';

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
				scores.map((score, index) => {
					return (
						<Bar score={score} index={index} {...props} {...scales} />
					);
				})
			}
		</svg>
	);
}
