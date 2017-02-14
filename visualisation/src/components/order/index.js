import { h, Component } from 'preact';
import style from './style';

import Country from '../country';

const countries = ['Ukraine','Belarus','Azerbaijan','Iceland','Norway','Romania','Armenia','Montenegro','Poland','Greece','Austria', 'Germany','Sweden','France','Russia','Italy','Slovenia','Finland','Spain','Switzerland','Hungary','Malta','Denmark','The Netherlands', 'San Marino','United Kingdom'];

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
				countries.map((country, index) => {
					const countryProps = {
						countryName: country,
						id: index,
						round: this.props.round
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
