import { h, Component } from 'preact';
import style from './style';

import Order from '../order';

export default class Home extends Component {
	render() {
		return (
			<div class={style.home}>
				<h1>Home</h1>
				<p>This is the Home component.</p>

				<Order />
			</div>
		);
	}
}
