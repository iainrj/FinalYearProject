import { h, Component } from 'preact';
import style from './style';

export default class About extends Component {
	state = {
		count: 0
	};

	// gets called when this route is navigated to
	componentDidMount() {
		// start a timer for the clock:
		this.timer = setInterval(::this.updateTime, 1000);
		this.updateTime();

		// every time we get remounted, increment a counter:
		this.setState({ count: this.state.count+1 });
	}

	// gets called just before navigating away from the route
	componentWillUnmount() {
		clearInterval(this.timer);
	}

	// update the current time
	updateTime() {
		let time = new Date().toLocaleString();
		this.setState({ time });
	}

	// Note: `user` comes from the URL, courtesy of our router
	render({ time, count }) {
		return (
			<div class={style.About}>
				<h1>About</h1>
				<p>This is the user About for a user named</p>

				<div>Current time: { time }</div>
				<div>About route mounted { count } times.</div>
			</div>
		);
	}
}
