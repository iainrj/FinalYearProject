import { h, Component } from 'preact';
import style from './style';

export default class About extends Component {
	render() {
		return (
			<div class={style.profile}>
				<h1>About</h1>
				<p>This is a project for a BSc in Computer Science final year project at Cardiff University</p>
				<p>In many elections or competitions, a set of voters will rank a set of candidates from best to worst, or will give scores to some of the candidates, with the winner then being the candidate that gets the highest total number of points. When it comes to revealing the result after all votes have been cast, some competitions proceed by having a roll-call of all the voters in which each announces their own scores.</p>
				<p>This is often done for entertainment purposes such as in the Eurovision Song Contest. The concept of entertainment, especially with respect to competition, is a heavily subjective subject and as such is hard to quantify in simple terms. There are intuitive constituent parts to an entertaining competition (like Eurovision) such as, if the winner is known early or late, and how many teams are in the running to win. A large constituent part of this project will be to convert these intuitive ideas into mathematical values that can then be maximised by some optimisation algorithm.</p>
				<p>The two main questions that this project will aim to answer are:</p>
				<ol>
					<li>How can we define the concept of ''entertainment'' in the context of an optimisation problem, and hence try to maximise it.</li>
					<li>In which order should the votes be revealed in order to maximise that entertainment value?</li>
				</ol>
				<p>This visualisation's aim is to aid in understanding why a solution to this problem is supposedly entertaining. The visualisation will play out the competition by revealing the votes in the order that the solution deems entertaining. From this it should be able to pinpoint the reasoning behind why the optimisation algorithms reached this solution.</p>
			</div>
		);
	}
}
