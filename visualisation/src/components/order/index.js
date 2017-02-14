import { h, Component } from 'preact';
import style from './style';

const countries = [
	{
		name: 'Ukraine',
		score: 0
	},
	{
		name: 'Belarus',
		score: 0
	},
	{
		name: 'Azerbaijan',
		score: 0
	},
	{
		name: 'Iceland',
		score: 0
	},
	{
		name: 'Norway',
		score: 0
	},
	{
		name: 'Romania',
		score: 0
	},
	{
		name: 'Armenia',
		score: 0
	},
	{
		name: 'Montenegro',
		score: 0
	},
	{
		name: 'Poland',
		score: 0
	},
	{
		name: 'Greece',
		score: 0
	},
	{
		name: 'Austria',
		score: 0
	},
	{
		name: 'Germany',
		score: 0
	},
	{
		name: 'Sweden',
		score: 0
	},
	{
		name: 'France',
		score: 0
	},
	{
		name: 'Russia',
		score: 0
	},
	{
		name: 'Italy',
		score: 0
	},
	{
		name: 'Slovenia',
		score: 0
	},
	{
		name: 'Finland',
		score: 0
	},
	{
		name: 'Spain',
		score: 0
	},
	{
		name: 'Switzerland',
		score: 0
	},
	{
		name: 'Hungary',
		score: 0
	},
	{
		name: 'Malta',
		score: 0
	},
	{
		name: 'Denmark',
		score: 0
	},
	{
		name: 'The Netherlands',
		score: 0
	},
	{
		name: 'San Marino',
		score: 0
	},
	{
		name: 'United Kingdom',
		score: 0
	}
];

export default class Order extends Component {
	render() {
		let float_styles = style.order_left;
		if (this.props.float === 'right') {
			float_styles = style.order_right;
		}

		return (
			<div class={float_styles}>
			<h2>{this.props.title}</h2>
			{
				countries.map((country) => {
					return (
						<ul class={style.countries_wrapper}>
							<li class={style.country_list_name}>{country.name}</li>
							<li class={style.country_list_score}>{country.score}</li>
						</ul>
					);
				})
			}

			</div>
		);
	}
}
