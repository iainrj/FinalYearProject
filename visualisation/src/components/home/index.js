import { h, Component } from 'preact';
import style from './style';

import Order from '../order';

export default class Home extends Component {
	constructor() {
		super();

		this.state.round = 0;
	}

	incrementRound() {
		this.setState({round: this.state.round + 1});
	}

	render() {
		return (
			<div class={style.home}>

				<h1>Round in order: {this.state.round}</h1>

				<center>
					<button class={style.round_incrementer} onClick={e => this.incrementRound()}>Next Round</button>
				</center>

				<Order float='left' title='Algorithms order'/>

				<Order float='right' title='Real world order'/>
			</div>
		);
	}
}
