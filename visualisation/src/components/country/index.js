import { h, Component } from 'preact';
import style from './style';

export default class Country extends Component {
	constructor() {
		super();

		this.state.score = 0;
	}

	componentWillReceiveProps(nextProps) {
		this.setState({score: this.state.score + nextProps.newScore});
	}

	componentWillUnmount() {
		this.setState({score: 0});
	}

	render() {
		return (
			<div class={style.country_wrapper}>
				<li key={this.props.countryName} class={style.country_list_name}>{this.props.countryName}</li>
				<li key={this.props.index} class={style.country_list_score}>{this.state.score}</li>
			</div>
		);
	}
}
