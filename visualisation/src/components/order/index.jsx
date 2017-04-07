import { h, Component } from 'preact';
import style from './style';
// import scoreboard from './scoreboard';

import Country from '../country';

const performers = ['Ukraine','Belarus','Azerbaijan','Iceland','Norway','Romania','Armenia','Montenegro','Poland','Greece','Austria', 'Germany','Sweden','France','Russia','Italy','Slovenia','Finland','Spain','Switzerland','Hungary','Malta','Denmark','The Netherlands', 'San Marino','United Kingdom'];

const voters = ['Albania', 'Armenia', 'Austria', 'Azerbaijan', 'Belarus', 'Belgium', 'Denmark', 'Estonia', 'FYR Macedonia', 'Finland', 'France','Georgia', 'Germany', 'Greece', 'Hungary', 'Iceland', 'Ireland', 'Israel', 'Italy', 'Latvia', 'Lithuania', 'Malta', 'Moldova', 'Montenegro', 'Norway', 'Poland', 'Portugal', 'Romania', 'Russia', 'San Marino', 'Slovenia', 'Spain', 'Sweden', 'Switzerland', 'The Netherlands', 'Ukraine', 'United Kingdom'];

const reveal_order = ['Azerbaijan','Greece','Poland','Albania','San Marino','Denmark','Montenegro','Romania','Russia','The Netherlands','Malta','France','United Kingdom','Latvia','Armenia','Iceland','FYR Macedonia','Sweden','Belarus','Germany','Israel','Portugal','Norway','Estonia','Hungary','Moldova','Ireland','Finland','Lithuania','Austria','Spain','Belgium','Italy','Ukraine','Switzerland','Georgia','Slovenia'];

export default class Order extends Component {
	render() {
		let float_styles = style.order_left;
		if (this.props.float === 'right') {
			float_styles = style.order_right;
		}

		return (
			<div class={float_styles}>
			<h2>{this.props.title}</h2>
			<ul class={style.countries_wrapper}>
			{
				performers.map((country, index) => {
					let country_scores = [];
					let c = performers.indexOf(country);

					for (let i = 0; i < voters.length; i++) {
						country_scores.push(scoreboard[c][i]);
					}

					const country_index = reveal_order[this.props.round];
					const score = country_scores[voters.indexOf(country_index)];

					const countryProps = {
						countryName: country,
						id: index,
						round: this.props.round,
						newScore: score
					};

					return (
						<Country {...countryProps}/>
					);
				})
			}
			</ul>
			</div>
		);
	}
}
