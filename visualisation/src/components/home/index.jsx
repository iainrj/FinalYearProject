import { h, Component } from 'preact';
import style from './style';

import Chart from '../chart';

export default class Home extends Component {
	constructor(props) {
		super(props);

		this.state.round = 0;
	}

	incrementRound(sim = false) {
		if (this.state.round < 37) {
			if (sim && !this._interval || this._interval !== 0) {
				this._interval = setInterval(() => (
					this.setState({round: this.state.round + 1})
				), 1000);

			} else {
				this.setState((prevState) => ({
					round: prevState.round + 1
				}));
			}

		}
	}

	stopSim() {
		clearInterval(this._interval);
		this._interval = 0;
	}

	componentWillUnmount() {
		this.stopSim();
	}

	resetCounter() {
		this.stopSim();

		this.setState({round: 0});
	}

	render() {
		return (
			<div class={style.home}>
				<div class={style.sim_controls}>
					<h2>Round in voting: {this.state.round}</h2>
					<button class={style.sim_controls__item} onClick={e => this.incrementRound(true)}>Start Sim</button>
					<button class={style.sim_controls__item} onClick={e => this.stopSim()}>Stop Sim</button>
					<button class={style.sim_controls__item} onClick={e => this.resetCounter()}>Reset</button>
				</div>

				<Chart {...this.state} />
			</div>
		);
	}
}
