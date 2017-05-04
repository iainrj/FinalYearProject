import { h, Component } from 'preact';
import style from './style';

import Chart from '../chart';
let int;

export default class Home extends Component {
	constructor(props) {
		super(props);

		this.state.round = 0;
		this.state.order = 'good';
	}

	incrementRound() {
		int = setInterval(() => {
			if (this.state.round < 37) {
				this.setState({round: this.state.round + 1});
			}
		}, 1300);
	}

	stopSim() {
		clearInterval(int);
	}

	componentWillUnmount() {
		this.stopSim();
	}

	resetCounter() {
		this.stopSim();
		location.reload();
	}

	handleChange(event) {
		this.setState({order: event.target.value});
	}

	render() {
		return (
			<div class={style.home}>
				<div class={style.sim_controls}>
					<h2>Round in voting: {this.state.round}</h2>
					<button class={style.sim_controls__item} onClick={e => this.incrementRound()}>Start Sim</button>
					<button class={style.sim_controls__item} onClick={e => this.stopSim()}>Stop Sim</button>
					<select class={style.sim_controls__item} value={this.state.order} onChange={e => this.handleChange(e)}>
						<option value="real">2014 Order</option>
						<option value="bad">Bad Order</option>
						<option value="good" selected>Good order</option>
					</select>
					<button class={style.sim_controls__item} onClick={e => this.resetCounter()}>Reset</button>
				</div>

				<Chart {...this.state} />
			</div>
		);
	}
}
