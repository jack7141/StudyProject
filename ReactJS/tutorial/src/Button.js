// Button 기능구현
import PropTypes from 'prop-types';
import styles from './Button.module.css';

function Button({ text }) {
    return <button className={styles.btn}>{text}</button>;
}

Button.prototype = {
    // Button 타입 정의
    text: PropTypes.string.isRequired,
};

export default Button;