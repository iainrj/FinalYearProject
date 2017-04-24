import { h, Component } from 'preact';
import style from './style';

import Chart from '../chart';

export default class Home extends Component {
	constructor(props) {
		super(props);

		this.state.round = 0;
	}

	interval(func, wait, times){
		let interv = function(w, t){
			return function(){
				if (typeof t === "undefined" || t-- > 0){
					setTimeout(interv, w);
					try {
						func.call(null);
					}
					catch (e){
						t = 0;
						throw e.toString();
					}
				}
			};
		}(wait, times);

		setTimeout(interv, wait);
	}

	incrementRound() {
		this.interval(() => {
			this.setState({round: this.state.round + 1});
		}, 1300, 37);
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
