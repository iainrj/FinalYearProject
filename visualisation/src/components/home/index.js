import { h, Component } from 'preact';
import style from './style';

import Order from '../order';

export default class Home extends Component {
	constructor() {
		super();

		this.state.round = 0;
	}

	incrementRound() {
		if (this.state.round < 37) {
			this.setState((prevState) => ({
				round: prevState.round + 1
			}));
		}
	}

	render() {
		return (
			<div class={style.home}>
				<center>
					<h1>Round in order: {this.state.round}</h1>
					<button class={style.round_incrementer} onClick={e => this.incrementRound()}>Next Round</button>
				</center>

				<Order float='left' title='Algorithms order' round={this.state.round}/>

				<Order float='right' title='Real world order' round={this.state.round}/>
			</div>
		);
	}
}
