// Generated from C:/Users/jxzk1/Desktop/xdrone-dsl/flask-backend/antlr\xDroneLexer.g4 by ANTLR 4.9.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class xDroneLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.9.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		MAIN=1, TAKEOFF=2, LAND=3, UP=4, DOWN=5, LEFT=6, RIGHT=7, FORWARD=8, BACKWARD=9, 
		ROTATE_LEFT=10, ROTATE_RIGHT=11, WAIT=12, AT=13, INSERT=14, REMOVE=15, 
		SIZE=16, IF=17, ELSE=18, WHILE=19, FOR=20, FROM=21, TO=22, STEP=23, REPEAT=24, 
		TIMES=25, DEL=26, FUNCTION=27, RETURN=28, TYPE_INT=29, TYPE_DECIMAL=30, 
		TYPE_STRING=31, TYPE_BOOLEAN=32, TYPE_VECTOR=33, TYPE_LIST=34, TRUE=35, 
		FALSE=36, VEC_X=37, VEC_Y=38, VEC_Z=39, MULTI=40, DIV=41, PLUS=42, MINUS=43, 
		CONCAT=44, GREATER=45, GREATER_EQ=46, LESS=47, LESS_EQ=48, EQ=49, NOT_EQ=50, 
		NOT=51, AND=52, OR=53, L_PAR=54, R_PAR=55, L_BRACKET=56, R_BRACKET=57, 
		L_BRACE=58, R_BRACE=59, DOT=60, COMMA=61, SEMICOLON=62, ARROW=63, COMMENT=64, 
		WS=65, IDENT=66, SIGNED_INT=67, SIGNED_FLOAT=68, ESCAPED_STRING=69;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"MAIN", "TAKEOFF", "LAND", "UP", "DOWN", "LEFT", "RIGHT", "FORWARD", 
			"BACKWARD", "ROTATE_LEFT", "ROTATE_RIGHT", "WAIT", "AT", "INSERT", "REMOVE", 
			"SIZE", "IF", "ELSE", "WHILE", "FOR", "FROM", "TO", "STEP", "REPEAT", 
			"TIMES", "DEL", "FUNCTION", "RETURN", "TYPE_INT", "TYPE_DECIMAL", "TYPE_STRING", 
			"TYPE_BOOLEAN", "TYPE_VECTOR", "TYPE_LIST", "TRUE", "FALSE", "VEC_X", 
			"VEC_Y", "VEC_Z", "MULTI", "DIV", "PLUS", "MINUS", "CONCAT", "GREATER", 
			"GREATER_EQ", "LESS", "LESS_EQ", "EQ", "NOT_EQ", "NOT", "AND", "OR", 
			"L_PAR", "R_PAR", "L_BRACKET", "R_BRACKET", "L_BRACE", "R_BRACE", "DOT", 
			"COMMA", "SEMICOLON", "ARROW", "DIGIT", "LOWERCASE", "UPPERCASE", "UNDERSCORE", 
			"COMMENT", "WS", "IDENT", "INT", "SIGNED_INT", "DECIMAL", "EXP", "FLOAT", 
			"SIGNED_FLOAT", "DOUBLE_QUOTE", "ESCAPED_CHAR", "CHARACTER", "ESCAPED_STRING"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'main'", "'takeoff'", "'land'", "'up'", "'down'", "'left'", "'right'", 
			"'forward'", "'backward'", "'rotate_left'", "'rotate_right'", "'wait'", 
			"'at'", "'insert'", "'remove'", "'size'", "'if'", "'else'", "'while'", 
			"'for'", "'from'", "'to'", "'step'", "'repeat'", "'times'", "'del'", 
			"'function'", "'return'", "'int'", "'decimal'", "'string'", "'boolean'", 
			"'vector'", "'list'", "'true'", "'false'", "'x'", "'y'", "'z'", "'*'", 
			"'/'", "'+'", "'-'", "'&'", "'>'", "'>='", "'<'", "'<='", "'=='", "'=/='", 
			"'not'", "'and'", "'or'", "'('", "')'", "'['", "']'", "'{'", "'}'", "'.'", 
			"','", "';'", "'<-'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "MAIN", "TAKEOFF", "LAND", "UP", "DOWN", "LEFT", "RIGHT", "FORWARD", 
			"BACKWARD", "ROTATE_LEFT", "ROTATE_RIGHT", "WAIT", "AT", "INSERT", "REMOVE", 
			"SIZE", "IF", "ELSE", "WHILE", "FOR", "FROM", "TO", "STEP", "REPEAT", 
			"TIMES", "DEL", "FUNCTION", "RETURN", "TYPE_INT", "TYPE_DECIMAL", "TYPE_STRING", 
			"TYPE_BOOLEAN", "TYPE_VECTOR", "TYPE_LIST", "TRUE", "FALSE", "VEC_X", 
			"VEC_Y", "VEC_Z", "MULTI", "DIV", "PLUS", "MINUS", "CONCAT", "GREATER", 
			"GREATER_EQ", "LESS", "LESS_EQ", "EQ", "NOT_EQ", "NOT", "AND", "OR", 
			"L_PAR", "R_PAR", "L_BRACKET", "R_BRACKET", "L_BRACE", "R_BRACE", "DOT", 
			"COMMA", "SEMICOLON", "ARROW", "COMMENT", "WS", "IDENT", "SIGNED_INT", 
			"SIGNED_FLOAT", "ESCAPED_STRING"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public xDroneLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "xDroneLexer.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2G\u022d\b\1\4\2\t"+
		"\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4"+
		",\t,\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t"+
		"\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t;\4<\t<\4=\t="+
		"\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I"+
		"\tI\4J\tJ\4K\tK\4L\tL\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\3\2\3\2\3\2\3\2\3"+
		"\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\6"+
		"\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3"+
		"\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3"+
		"\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3"+
		"\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\17"+
		"\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21"+
		"\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\24\3\24"+
		"\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\27"+
		"\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31"+
		"\3\32\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34"+
		"\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36"+
		"\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3 \3 \3"+
		" \3!\3!\3!\3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\3"+
		"$\3$\3$\3$\3$\3%\3%\3%\3%\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+"+
		"\3,\3,\3-\3-\3.\3.\3/\3/\3/\3\60\3\60\3\61\3\61\3\61\3\62\3\62\3\62\3"+
		"\63\3\63\3\63\3\63\3\64\3\64\3\64\3\64\3\65\3\65\3\65\3\65\3\66\3\66\3"+
		"\66\3\67\3\67\38\38\39\39\3:\3:\3;\3;\3<\3<\3=\3=\3>\3>\3?\3?\3@\3@\3"+
		"@\3A\3A\3B\3B\3C\3C\3D\3D\3E\3E\7E\u01cb\nE\fE\16E\u01ce\13E\3E\3E\3E"+
		"\3E\3F\6F\u01d5\nF\rF\16F\u01d6\3F\3F\3G\3G\3G\5G\u01de\nG\3G\3G\3G\3"+
		"G\7G\u01e4\nG\fG\16G\u01e7\13G\3H\6H\u01ea\nH\rH\16H\u01eb\3I\5I\u01ef"+
		"\nI\3I\3I\3J\3J\3J\5J\u01f6\nJ\3J\3J\5J\u01fa\nJ\3K\3K\3K\3L\3L\3L\3L"+
		"\3L\5L\u0204\nL\5L\u0206\nL\3M\5M\u0209\nM\3M\3M\3N\3N\3O\3O\3O\3O\3O"+
		"\3O\3O\3O\3O\3O\3O\3O\3O\3O\3O\3O\5O\u021f\nO\3P\3P\5P\u0223\nP\3Q\3Q"+
		"\7Q\u0227\nQ\fQ\16Q\u022a\13Q\3Q\3Q\2\2R\3\3\5\4\7\5\t\6\13\7\r\b\17\t"+
		"\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27"+
		"-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W"+
		"-Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8o9q:s;u<w=y>{?}@\177A\u0081\2\u0083"+
		"\2\u0085\2\u0087\2\u0089B\u008bC\u008dD\u008f\2\u0091E\u0093\2\u0095\2"+
		"\u0097\2\u0099F\u009b\2\u009d\2\u009f\2\u00a1G\3\2\n\3\2\62;\3\2c|\3\2"+
		"C\\\4\2\f\f\17\17\5\2\13\f\17\17\"\"\4\2--//\4\2GGgg\5\2$$))^^\2\u0239"+
		"\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2"+
		"\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2"+
		"\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2"+
		"\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2"+
		"\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3"+
		"\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2"+
		"\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2"+
		"U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3"+
		"\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2"+
		"\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2"+
		"{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d"+
		"\3\2\2\2\2\u0091\3\2\2\2\2\u0099\3\2\2\2\2\u00a1\3\2\2\2\3\u00a3\3\2\2"+
		"\2\5\u00a8\3\2\2\2\7\u00b0\3\2\2\2\t\u00b5\3\2\2\2\13\u00b8\3\2\2\2\r"+
		"\u00bd\3\2\2\2\17\u00c2\3\2\2\2\21\u00c8\3\2\2\2\23\u00d0\3\2\2\2\25\u00d9"+
		"\3\2\2\2\27\u00e5\3\2\2\2\31\u00f2\3\2\2\2\33\u00f7\3\2\2\2\35\u00fa\3"+
		"\2\2\2\37\u0101\3\2\2\2!\u0108\3\2\2\2#\u010d\3\2\2\2%\u0110\3\2\2\2\'"+
		"\u0115\3\2\2\2)\u011b\3\2\2\2+\u011f\3\2\2\2-\u0124\3\2\2\2/\u0127\3\2"+
		"\2\2\61\u012c\3\2\2\2\63\u0133\3\2\2\2\65\u0139\3\2\2\2\67\u013d\3\2\2"+
		"\29\u0146\3\2\2\2;\u014d\3\2\2\2=\u0151\3\2\2\2?\u0159\3\2\2\2A\u0160"+
		"\3\2\2\2C\u0168\3\2\2\2E\u016f\3\2\2\2G\u0174\3\2\2\2I\u0179\3\2\2\2K"+
		"\u017f\3\2\2\2M\u0181\3\2\2\2O\u0183\3\2\2\2Q\u0185\3\2\2\2S\u0187\3\2"+
		"\2\2U\u0189\3\2\2\2W\u018b\3\2\2\2Y\u018d\3\2\2\2[\u018f\3\2\2\2]\u0191"+
		"\3\2\2\2_\u0194\3\2\2\2a\u0196\3\2\2\2c\u0199\3\2\2\2e\u019c\3\2\2\2g"+
		"\u01a0\3\2\2\2i\u01a4\3\2\2\2k\u01a8\3\2\2\2m\u01ab\3\2\2\2o\u01ad\3\2"+
		"\2\2q\u01af\3\2\2\2s\u01b1\3\2\2\2u\u01b3\3\2\2\2w\u01b5\3\2\2\2y\u01b7"+
		"\3\2\2\2{\u01b9\3\2\2\2}\u01bb\3\2\2\2\177\u01bd\3\2\2\2\u0081\u01c0\3"+
		"\2\2\2\u0083\u01c2\3\2\2\2\u0085\u01c4\3\2\2\2\u0087\u01c6\3\2\2\2\u0089"+
		"\u01c8\3\2\2\2\u008b\u01d4\3\2\2\2\u008d\u01dd\3\2\2\2\u008f\u01e9\3\2"+
		"\2\2\u0091\u01ee\3\2\2\2\u0093\u01f9\3\2\2\2\u0095\u01fb\3\2\2\2\u0097"+
		"\u0205\3\2\2\2\u0099\u0208\3\2\2\2\u009b\u020c\3\2\2\2\u009d\u021e\3\2"+
		"\2\2\u009f\u0222\3\2\2\2\u00a1\u0224\3\2\2\2\u00a3\u00a4\7o\2\2\u00a4"+
		"\u00a5\7c\2\2\u00a5\u00a6\7k\2\2\u00a6\u00a7\7p\2\2\u00a7\4\3\2\2\2\u00a8"+
		"\u00a9\7v\2\2\u00a9\u00aa\7c\2\2\u00aa\u00ab\7m\2\2\u00ab\u00ac\7g\2\2"+
		"\u00ac\u00ad\7q\2\2\u00ad\u00ae\7h\2\2\u00ae\u00af\7h\2\2\u00af\6\3\2"+
		"\2\2\u00b0\u00b1\7n\2\2\u00b1\u00b2\7c\2\2\u00b2\u00b3\7p\2\2\u00b3\u00b4"+
		"\7f\2\2\u00b4\b\3\2\2\2\u00b5\u00b6\7w\2\2\u00b6\u00b7\7r\2\2\u00b7\n"+
		"\3\2\2\2\u00b8\u00b9\7f\2\2\u00b9\u00ba\7q\2\2\u00ba\u00bb\7y\2\2\u00bb"+
		"\u00bc\7p\2\2\u00bc\f\3\2\2\2\u00bd\u00be\7n\2\2\u00be\u00bf\7g\2\2\u00bf"+
		"\u00c0\7h\2\2\u00c0\u00c1\7v\2\2\u00c1\16\3\2\2\2\u00c2\u00c3\7t\2\2\u00c3"+
		"\u00c4\7k\2\2\u00c4\u00c5\7i\2\2\u00c5\u00c6\7j\2\2\u00c6\u00c7\7v\2\2"+
		"\u00c7\20\3\2\2\2\u00c8\u00c9\7h\2\2\u00c9\u00ca\7q\2\2\u00ca\u00cb\7"+
		"t\2\2\u00cb\u00cc\7y\2\2\u00cc\u00cd\7c\2\2\u00cd\u00ce\7t\2\2\u00ce\u00cf"+
		"\7f\2\2\u00cf\22\3\2\2\2\u00d0\u00d1\7d\2\2\u00d1\u00d2\7c\2\2\u00d2\u00d3"+
		"\7e\2\2\u00d3\u00d4\7m\2\2\u00d4\u00d5\7y\2\2\u00d5\u00d6\7c\2\2\u00d6"+
		"\u00d7\7t\2\2\u00d7\u00d8\7f\2\2\u00d8\24\3\2\2\2\u00d9\u00da\7t\2\2\u00da"+
		"\u00db\7q\2\2\u00db\u00dc\7v\2\2\u00dc\u00dd\7c\2\2\u00dd\u00de\7v\2\2"+
		"\u00de\u00df\7g\2\2\u00df\u00e0\7a\2\2\u00e0\u00e1\7n\2\2\u00e1\u00e2"+
		"\7g\2\2\u00e2\u00e3\7h\2\2\u00e3\u00e4\7v\2\2\u00e4\26\3\2\2\2\u00e5\u00e6"+
		"\7t\2\2\u00e6\u00e7\7q\2\2\u00e7\u00e8\7v\2\2\u00e8\u00e9\7c\2\2\u00e9"+
		"\u00ea\7v\2\2\u00ea\u00eb\7g\2\2\u00eb\u00ec\7a\2\2\u00ec\u00ed\7t\2\2"+
		"\u00ed\u00ee\7k\2\2\u00ee\u00ef\7i\2\2\u00ef\u00f0\7j\2\2\u00f0\u00f1"+
		"\7v\2\2\u00f1\30\3\2\2\2\u00f2\u00f3\7y\2\2\u00f3\u00f4\7c\2\2\u00f4\u00f5"+
		"\7k\2\2\u00f5\u00f6\7v\2\2\u00f6\32\3\2\2\2\u00f7\u00f8\7c\2\2\u00f8\u00f9"+
		"\7v\2\2\u00f9\34\3\2\2\2\u00fa\u00fb\7k\2\2\u00fb\u00fc\7p\2\2\u00fc\u00fd"+
		"\7u\2\2\u00fd\u00fe\7g\2\2\u00fe\u00ff\7t\2\2\u00ff\u0100\7v\2\2\u0100"+
		"\36\3\2\2\2\u0101\u0102\7t\2\2\u0102\u0103\7g\2\2\u0103\u0104\7o\2\2\u0104"+
		"\u0105\7q\2\2\u0105\u0106\7x\2\2\u0106\u0107\7g\2\2\u0107 \3\2\2\2\u0108"+
		"\u0109\7u\2\2\u0109\u010a\7k\2\2\u010a\u010b\7|\2\2\u010b\u010c\7g\2\2"+
		"\u010c\"\3\2\2\2\u010d\u010e\7k\2\2\u010e\u010f\7h\2\2\u010f$\3\2\2\2"+
		"\u0110\u0111\7g\2\2\u0111\u0112\7n\2\2\u0112\u0113\7u\2\2\u0113\u0114"+
		"\7g\2\2\u0114&\3\2\2\2\u0115\u0116\7y\2\2\u0116\u0117\7j\2\2\u0117\u0118"+
		"\7k\2\2\u0118\u0119\7n\2\2\u0119\u011a\7g\2\2\u011a(\3\2\2\2\u011b\u011c"+
		"\7h\2\2\u011c\u011d\7q\2\2\u011d\u011e\7t\2\2\u011e*\3\2\2\2\u011f\u0120"+
		"\7h\2\2\u0120\u0121\7t\2\2\u0121\u0122\7q\2\2\u0122\u0123\7o\2\2\u0123"+
		",\3\2\2\2\u0124\u0125\7v\2\2\u0125\u0126\7q\2\2\u0126.\3\2\2\2\u0127\u0128"+
		"\7u\2\2\u0128\u0129\7v\2\2\u0129\u012a\7g\2\2\u012a\u012b\7r\2\2\u012b"+
		"\60\3\2\2\2\u012c\u012d\7t\2\2\u012d\u012e\7g\2\2\u012e\u012f\7r\2\2\u012f"+
		"\u0130\7g\2\2\u0130\u0131\7c\2\2\u0131\u0132\7v\2\2\u0132\62\3\2\2\2\u0133"+
		"\u0134\7v\2\2\u0134\u0135\7k\2\2\u0135\u0136\7o\2\2\u0136\u0137\7g\2\2"+
		"\u0137\u0138\7u\2\2\u0138\64\3\2\2\2\u0139\u013a\7f\2\2\u013a\u013b\7"+
		"g\2\2\u013b\u013c\7n\2\2\u013c\66\3\2\2\2\u013d\u013e\7h\2\2\u013e\u013f"+
		"\7w\2\2\u013f\u0140\7p\2\2\u0140\u0141\7e\2\2\u0141\u0142\7v\2\2\u0142"+
		"\u0143\7k\2\2\u0143\u0144\7q\2\2\u0144\u0145\7p\2\2\u01458\3\2\2\2\u0146"+
		"\u0147\7t\2\2\u0147\u0148\7g\2\2\u0148\u0149\7v\2\2\u0149\u014a\7w\2\2"+
		"\u014a\u014b\7t\2\2\u014b\u014c\7p\2\2\u014c:\3\2\2\2\u014d\u014e\7k\2"+
		"\2\u014e\u014f\7p\2\2\u014f\u0150\7v\2\2\u0150<\3\2\2\2\u0151\u0152\7"+
		"f\2\2\u0152\u0153\7g\2\2\u0153\u0154\7e\2\2\u0154\u0155\7k\2\2\u0155\u0156"+
		"\7o\2\2\u0156\u0157\7c\2\2\u0157\u0158\7n\2\2\u0158>\3\2\2\2\u0159\u015a"+
		"\7u\2\2\u015a\u015b\7v\2\2\u015b\u015c\7t\2\2\u015c\u015d\7k\2\2\u015d"+
		"\u015e\7p\2\2\u015e\u015f\7i\2\2\u015f@\3\2\2\2\u0160\u0161\7d\2\2\u0161"+
		"\u0162\7q\2\2\u0162\u0163\7q\2\2\u0163\u0164\7n\2\2\u0164\u0165\7g\2\2"+
		"\u0165\u0166\7c\2\2\u0166\u0167\7p\2\2\u0167B\3\2\2\2\u0168\u0169\7x\2"+
		"\2\u0169\u016a\7g\2\2\u016a\u016b\7e\2\2\u016b\u016c\7v\2\2\u016c\u016d"+
		"\7q\2\2\u016d\u016e\7t\2\2\u016eD\3\2\2\2\u016f\u0170\7n\2\2\u0170\u0171"+
		"\7k\2\2\u0171\u0172\7u\2\2\u0172\u0173\7v\2\2\u0173F\3\2\2\2\u0174\u0175"+
		"\7v\2\2\u0175\u0176\7t\2\2\u0176\u0177\7w\2\2\u0177\u0178\7g\2\2\u0178"+
		"H\3\2\2\2\u0179\u017a\7h\2\2\u017a\u017b\7c\2\2\u017b\u017c\7n\2\2\u017c"+
		"\u017d\7u\2\2\u017d\u017e\7g\2\2\u017eJ\3\2\2\2\u017f\u0180\7z\2\2\u0180"+
		"L\3\2\2\2\u0181\u0182\7{\2\2\u0182N\3\2\2\2\u0183\u0184\7|\2\2\u0184P"+
		"\3\2\2\2\u0185\u0186\7,\2\2\u0186R\3\2\2\2\u0187\u0188\7\61\2\2\u0188"+
		"T\3\2\2\2\u0189\u018a\7-\2\2\u018aV\3\2\2\2\u018b\u018c\7/\2\2\u018cX"+
		"\3\2\2\2\u018d\u018e\7(\2\2\u018eZ\3\2\2\2\u018f\u0190\7@\2\2\u0190\\"+
		"\3\2\2\2\u0191\u0192\7@\2\2\u0192\u0193\7?\2\2\u0193^\3\2\2\2\u0194\u0195"+
		"\7>\2\2\u0195`\3\2\2\2\u0196\u0197\7>\2\2\u0197\u0198\7?\2\2\u0198b\3"+
		"\2\2\2\u0199\u019a\7?\2\2\u019a\u019b\7?\2\2\u019bd\3\2\2\2\u019c\u019d"+
		"\7?\2\2\u019d\u019e\7\61\2\2\u019e\u019f\7?\2\2\u019ff\3\2\2\2\u01a0\u01a1"+
		"\7p\2\2\u01a1\u01a2\7q\2\2\u01a2\u01a3\7v\2\2\u01a3h\3\2\2\2\u01a4\u01a5"+
		"\7c\2\2\u01a5\u01a6\7p\2\2\u01a6\u01a7\7f\2\2\u01a7j\3\2\2\2\u01a8\u01a9"+
		"\7q\2\2\u01a9\u01aa\7t\2\2\u01aal\3\2\2\2\u01ab\u01ac\7*\2\2\u01acn\3"+
		"\2\2\2\u01ad\u01ae\7+\2\2\u01aep\3\2\2\2\u01af\u01b0\7]\2\2\u01b0r\3\2"+
		"\2\2\u01b1\u01b2\7_\2\2\u01b2t\3\2\2\2\u01b3\u01b4\7}\2\2\u01b4v\3\2\2"+
		"\2\u01b5\u01b6\7\177\2\2\u01b6x\3\2\2\2\u01b7\u01b8\7\60\2\2\u01b8z\3"+
		"\2\2\2\u01b9\u01ba\7.\2\2\u01ba|\3\2\2\2\u01bb\u01bc\7=\2\2\u01bc~\3\2"+
		"\2\2\u01bd\u01be\7>\2\2\u01be\u01bf\7/\2\2\u01bf\u0080\3\2\2\2\u01c0\u01c1"+
		"\t\2\2\2\u01c1\u0082\3\2\2\2\u01c2\u01c3\t\3\2\2\u01c3\u0084\3\2\2\2\u01c4"+
		"\u01c5\t\4\2\2\u01c5\u0086\3\2\2\2\u01c6\u01c7\7a\2\2\u01c7\u0088\3\2"+
		"\2\2\u01c8\u01cc\7%\2\2\u01c9\u01cb\n\5\2\2\u01ca\u01c9\3\2\2\2\u01cb"+
		"\u01ce\3\2\2\2\u01cc\u01ca\3\2\2\2\u01cc\u01cd\3\2\2\2\u01cd\u01cf\3\2"+
		"\2\2\u01ce\u01cc\3\2\2\2\u01cf\u01d0\t\5\2\2\u01d0\u01d1\3\2\2\2\u01d1"+
		"\u01d2\bE\2\2\u01d2\u008a\3\2\2\2\u01d3\u01d5\t\6\2\2\u01d4\u01d3\3\2"+
		"\2\2\u01d5\u01d6\3\2\2\2\u01d6\u01d4\3\2\2\2\u01d6\u01d7\3\2\2\2\u01d7"+
		"\u01d8\3\2\2\2\u01d8\u01d9\bF\2\2\u01d9\u008c\3\2\2\2\u01da\u01de\5\u0087"+
		"D\2\u01db\u01de\5\u0083B\2\u01dc\u01de\5\u0085C\2\u01dd\u01da\3\2\2\2"+
		"\u01dd\u01db\3\2\2\2\u01dd\u01dc\3\2\2\2\u01de\u01e5\3\2\2\2\u01df\u01e4"+
		"\5\u0087D\2\u01e0\u01e4\5\u0083B\2\u01e1\u01e4\5\u0085C\2\u01e2\u01e4"+
		"\5\u0081A\2\u01e3\u01df\3\2\2\2\u01e3\u01e0\3\2\2\2\u01e3\u01e1\3\2\2"+
		"\2\u01e3\u01e2\3\2\2\2\u01e4\u01e7\3\2\2\2\u01e5\u01e3\3\2\2\2\u01e5\u01e6"+
		"\3\2\2\2\u01e6\u008e\3\2\2\2\u01e7\u01e5\3\2\2\2\u01e8\u01ea\5\u0081A"+
		"\2\u01e9\u01e8\3\2\2\2\u01ea\u01eb\3\2\2\2\u01eb\u01e9\3\2\2\2\u01eb\u01ec"+
		"\3\2\2\2\u01ec\u0090\3\2\2\2\u01ed\u01ef\t\7\2\2\u01ee\u01ed\3\2\2\2\u01ee"+
		"\u01ef\3\2\2\2\u01ef\u01f0\3\2\2\2\u01f0\u01f1\5\u008fH\2\u01f1\u0092"+
		"\3\2\2\2\u01f2\u01f3\5\u008fH\2\u01f3\u01f5\7\60\2\2\u01f4\u01f6\5\u008f"+
		"H\2\u01f5\u01f4\3\2\2\2\u01f5\u01f6\3\2\2\2\u01f6\u01fa\3\2\2\2\u01f7"+
		"\u01f8\7\60\2\2\u01f8\u01fa\5\u008fH\2\u01f9\u01f2\3\2\2\2\u01f9\u01f7"+
		"\3\2\2\2\u01fa\u0094\3\2\2\2\u01fb\u01fc\t\b\2\2\u01fc\u01fd\5\u0091I"+
		"\2\u01fd\u0096\3\2\2\2\u01fe\u01ff\5\u008fH\2\u01ff\u0200\5\u0095K\2\u0200"+
		"\u0206\3\2\2\2\u0201\u0203\5\u0093J\2\u0202\u0204\5\u0095K\2\u0203\u0202"+
		"\3\2\2\2\u0203\u0204\3\2\2\2\u0204\u0206\3\2\2\2\u0205\u01fe\3\2\2\2\u0205"+
		"\u0201\3\2\2\2\u0206\u0098\3\2\2\2\u0207\u0209\t\7\2\2\u0208\u0207\3\2"+
		"\2\2\u0208\u0209\3\2\2\2\u0209\u020a\3\2\2\2\u020a\u020b\5\u0097L\2\u020b"+
		"\u009a\3\2\2\2\u020c\u020d\7$\2\2\u020d\u009c\3\2\2\2\u020e\u020f\7^\2"+
		"\2\u020f\u021f\7\62\2\2\u0210\u0211\7^\2\2\u0211\u021f\7d\2\2\u0212\u0213"+
		"\7^\2\2\u0213\u021f\7p\2\2\u0214\u0215\7^\2\2\u0215\u021f\7h\2\2\u0216"+
		"\u0217\7^\2\2\u0217\u021f\7t\2\2\u0218\u0219\7^\2\2\u0219\u021f\5\u009b"+
		"N\2\u021a\u021b\7^\2\2\u021b\u021f\7)\2\2\u021c\u021d\7^\2\2\u021d\u021f"+
		"\7^\2\2\u021e\u020e\3\2\2\2\u021e\u0210\3\2\2\2\u021e\u0212\3\2\2\2\u021e"+
		"\u0214\3\2\2\2\u021e\u0216\3\2\2\2\u021e\u0218\3\2\2\2\u021e\u021a\3\2"+
		"\2\2\u021e\u021c\3\2\2\2\u021f\u009e\3\2\2\2\u0220\u0223\n\t\2\2\u0221"+
		"\u0223\5\u009dO\2\u0222\u0220\3\2\2\2\u0222\u0221\3\2\2\2\u0223\u00a0"+
		"\3\2\2\2\u0224\u0228\5\u009bN\2\u0225\u0227\5\u009fP\2\u0226\u0225\3\2"+
		"\2\2\u0227\u022a\3\2\2\2\u0228\u0226\3\2\2\2\u0228\u0229\3\2\2\2\u0229"+
		"\u022b\3\2\2\2\u022a\u0228\3\2\2\2\u022b\u022c\5\u009bN\2\u022c\u00a2"+
		"\3\2\2\2\22\2\u01cc\u01d6\u01dd\u01e3\u01e5\u01eb\u01ee\u01f5\u01f9\u0203"+
		"\u0205\u0208\u021e\u0222\u0228\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}